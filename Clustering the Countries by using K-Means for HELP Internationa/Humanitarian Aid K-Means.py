#!/usr/bin/env python
# coding: utf-8

# ## 1. import required libraries

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


import sklearn
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans


# ## 2. Read and Understand the data set

# In[10]:


df = pd.read_csv('Data_Negara_HELP.csv')
df.head()


# In[11]:


# Memeriksa jumlah kolom dan baris dataframe menggunakan shape function
df.shape


# In[12]:


# MEngecek informasi dataset
df.info()


# In[13]:


# mengecek statistik deskriptif
df.describe()


# In[14]:


# mengecek nama kolom
df.columns


# Insights:
# 
# - Data set terdiri dari 167 Negara dimana masing-masing memiliki 10 fitur.
# - Tidak ada missing value ataupun duplikat dari dataset
# - Referring to data dictionary, exports, health and imports are given as %age of GDP per capita. So lets convert it to actual value

# In[15]:


# Memastikan jumlah missing value
df.isnull().sum()


# Kita akan mengubah nilai impor, ekspor dan kesehatan dari nilai persentase ke nilai aktual PDB per kapita, karena nilai persentase tidak memberikan gambaran yang jelas tentang negara itu.
# 
# Seperti: - Austria dan Belarus memiliki % ekspor yang hampir sama tetapi gdpp mereka memiliki kesenjangan besar dan tidak memberikan gambaran yang akurat tentang negara mana yang lebih maju daripada yang lain. Kemudian kita akan menghapus kolom Negara dan menyimpannya sebagai nama baris dalam dataframe akhir.

# In[19]:


# mengubah import, export dan kesehatan dari persentasi menjadi nilai absolut dengan menggunakan kolom GDB/Kapita.

df['Impor'] = df['Impor'] * df['GDPperkapita']/100
df['Ekspor'] = df['Ekspor'] * df['GDPperkapita']/100
df['Kesehatan'] = df['Kesehatan'] * df['GDPperkapita']/100

df.head()


# In[20]:


# Mengecek shape dari dataframe baru
df.shape


# In[21]:


# memilih numerical columns dan drop negara dan melihat persentil masing-masing data
cols = ['Ekspor', 'Kesehatan', 'Impor', 'Jumlah_fertiliti','GDPperkapita']
df[cols].describe(percentiles= [0.01,0.25,0.5,0.75,0.99])


# ## 3. Exploratory Data Analytics (EDA)

# Exploratory Data Analysis (EDA) adalah bagian dari proses data science. EDA menjadi sangat penting sebelum melakukan feature engineering dan modeling karena dalam tahap ini kita harus memahami datanya terlebih dahulu.

# In[22]:


# melihat outliers pada persentil 25%,50%,75%,90%,95% dan 99%
df.describe(percentiles=[.25,.5,.75,.90,.95,.99])


# In[66]:


# mengecek outliers dengan boxplot
fig, axs = plt.subplots(3,3, figsize = (16,8))

plt1 = sns.boxplot(df['Kematian_anak'], ax = axs[0,0], color = 'orange')
plt2 = sns.boxplot(df['Ekspor'], ax = axs[0,1])
plt3 = sns.boxplot(df['Kesehatan'], ax = axs[0,2], color = 'orange')
plt4 = sns.boxplot(df['Impor'], ax = axs[1,0])
plt5 = sns.boxplot(df['Pendapatan'], ax = axs[1,1], color = 'orange')
plt6 = sns.boxplot(df['Inflasi'], ax = axs[1,2])
plt7 = sns.boxplot(df['Harapan_hidup'], ax = axs[2,0], color = 'orange')
plt8 = sns.boxplot(df['Jumlah_fertiliti'], ax = axs[2,1])
plt9 = sns.boxplot(df['GDPperkapita'], ax = axs[2,2], color = 'orange')

plt.show()


# Insight:
# 
# Dari data diatas, kita mendapatkan beberapa Outliers, nanti akan kita lakukan Handling Outliers
# 
# ----

# Pada tahap ini, kita akan coba untuk mengecek daftar 10 negara termiskin dari tiap-tiap fitur yang tersedia dengan menggunakan barplot

# In[27]:


df.columns


# In[30]:


fig, axs = plt.subplots(3,3,figsize = (12,12))

# poor top 10 countries represented as `pt10`

# Child Mortality Rate 
pt10_Kematian_anak = df[['Negara','Kematian_anak']].sort_values('Kematian_anak', ascending = False).head(10)
plt1 = sns.barplot(x='Negara', y='Kematian_anak', data= pt10_Kematian_anak, ax = axs[0,0])
plt1.set(xlabel = '', ylabel= 'Rate Kematian_anak')

# Exports
pt10_Ekspor = df[['Negara','Ekspor']].sort_values('Ekspor', ascending = True).head(10)
plt2 = sns.barplot(x='Negara', y='Ekspor', data= pt10_Ekspor, ax = axs[2,1])
plt2.set(xlabel = '', ylabel= 'Ekspor')

# Health 
pt10_Kesehatan = df[['Negara','Kesehatan']].sort_values('Kesehatan', ascending = True).head(10)
plt3 = sns.barplot(x='Negara', y='Kesehatan', data= pt10_Kesehatan, ax = axs[1,0])
plt3.set(xlabel = '', ylabel= 'Kesehatan')

# Imports
pt10_Impor = df[['Negara','Impor']].sort_values('Impor', ascending = True).head(10)
plt4 = sns.barplot(x='Negara', y='Impor', data= pt10_Impor, ax = axs[2,2])
plt4.set(xlabel = '', ylabel= 'Impor')

# Per capita Income 
pt10_Pendapatan = df[['Negara','Pendapatan']].sort_values('Pendapatan', ascending = True).head(10)
plt5 = sns.barplot(x='Negara', y='Pendapatan', data= pt10_Pendapatan, ax = axs[1,2])
plt5.set(xlabel = '', ylabel= 'Pendapatan')

# Inflation
pt10_Inflasi = df[['Negara','Inflasi']].sort_values('Inflasi', ascending = False).head(10)
plt6 = sns.barplot(x='Negara', y='Inflasi', data= pt10_Inflasi, ax = axs[2,0])
plt6.set(xlabel = '', ylabel= 'Inflasi')

# Fertility Rate
pt10_Jumlah_fertiliti = df[['Negara','Jumlah_fertiliti']].sort_values('Jumlah_fertiliti', ascending = False).head(10)
plt7 = sns.barplot(x='Negara', y='Jumlah_fertiliti', data= pt10_Jumlah_fertiliti, ax = axs[0,1])
plt7.set(xlabel = '', ylabel= 'Jumlah_fertiliti')

# Life Expectancy
pt10_Harapan_hidup = df[['Negara','Harapan_hidup']].sort_values('Harapan_hidup', ascending = True).head(10)
plt8 = sns.barplot(x='Negara', y='Harapan_hidup', data= pt10_Harapan_hidup, ax = axs[0,2])
plt8.set(xlabel = '', ylabel= 'Harapan_hidup')

# The GDP per capita 
pt10_GDPperkapita = df[['Negara','GDPperkapita']].sort_values('GDPperkapita', ascending = True).head(10)
plt9 = sns.barplot(x='Negara', y='GDPperkapita', data= pt10_GDPperkapita, ax = axs[1,1])
plt9.set(xlabel = '', ylabel= 'GDP per capita')


for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation = 90)
    
plt.tight_layout()
plt.show()


# Insight:
# 
# - Dari data diatas, kita dapat melihat negara-negara yang paling banyak termasuk dalam negara termiskin berdasarkan GDP perkapita, Keatian anak, dan pendapatan adalah: Congo, Dem. Rep., Niger, Sierra Leone,Central African Republic

# In[31]:


# Plot Ditribusi
plt.figure(figsize=(15, 15))
features = ['Kematian_anak', 'Ekspor', 'Kesehatan', 'Impor', 'Pendapatan',
       'Inflasi', 'Harapan_hidup', 'Jumlah_fertiliti', 'GDPperkapita']
for i in enumerate(features):
    ax = plt.subplot(3, 3, i[0]+1)
    sns.distplot(df[i[1]])
    plt.xticks(rotation=20)


# Insights:
# 
# - selain harapan hidup, semua kolom terdistribusi miring kekiri

# In[59]:


# Melihat korelasi dataset
plt.figure(figsize= (12,8))
sns.heatmap(df.corr(), annot = True, cmap = "GnBu")


# Dari plotting diatas, kita dapat mengambil beberapa kesimpulan bahwa terdapat beberapa fitur yang memilihi korelasi tinggi
# 
# - GDP per Kapita dan pendapatan memiliki korelasi yang tinggi yaitu 0.9
# - Kematian anak dan harapan hidup memiliki korelasi negatif yang tinggi, yaitu sebesar -0.89
# - Kematian anak dan jumlah fertilisasi memiliki korelasi yang sangat tinggi, yaitu sebesar 0.85
# - Import dan eksport memiliki korelasi yang cukup tinggi, yaitu of 0.74
# - Harapan hidup dan jumlah fertilisasi emiliki korelasi negatif yang cukup tinngi, yaitu -0.76
# ----

# **Handling Outliers**
# - kematian anak, ekspor dan harapan hidup memiliki outliers dengan level tinggi, jika data diatas persentil 99% kita akan melakukan drop dataset

# In[35]:


# Kita drop kolom negara
df1 = df.drop('Negara', axis =1)


# In[36]:


# daftar kolom yang memiliki outliers persentil 99%
cols = [ 'Ekspor', 'Kesehatan', 'Impor', 
        'Jumlah_fertiliti', 'GDPperkapita']
df1[cols].describe(percentiles= [0.01,0.25,0.5,0.75,0.99])


# In[37]:


# kita akan menghandling outliers persentil 99%
cap = 0.99
for col in cols:
    HL = round(df1[col].quantile(cap),2)
    df1[col] = df1[col].apply(lambda x: HL if x>HL else x)


# In[38]:


df1[cols].describe(percentiles= [0.01,0.25,0.5,0.75,0.99])


# In[39]:


# Cek outliers setelah handling outliers dengan menggunakan boxplot
df1[cols].plot.box(subplots = True, figsize = (18,6), fontsize = 12)
plt.tight_layout(pad=3)
plt.show()


# dari data diatas, memang masih ada outliers namun kita masih dapat melanjutkan proses kita
# 
# ---

# ## 4. Feature Scaling

# In[40]:


# mengecek nama kolom dataset
df1.columns


# In[42]:


# kita akan melakukan sclaling dengan MinMaxScaller
scaler = MinMaxScaler()

df_scaled = scaler.fit_transform(df1)
df_scaled.shape


# In[43]:


df_scaled


# ## 5. Clustering

# Pada proses clustering, kita akan menggunakan algoritma K-Means clustering. K-Means adalah suatu metode penganalisaan data atau metode Data Mining yang melakukan proses pemodelan tanpa supervisi (unsupervised) dan merupakan salah satu metode yang melakukan pengelompokan data dengan sistem partisi. Metode k-means berusaha mengelompokkan data yang ada ke dalam beberapa kelompok, dimana data dalam satu kelompok mempunyai karakteristik yang sama satu sama lainnya dan mempunyai karakteristik yang berbeda dengan data yang ada di dalam kelompok yang lain. Dengan kata lain, metode ini berusaha untuk meminimalkan variasi antar data yang ada di dalam suatu cluster dan memaksimalkan variasi dengan data yang ada di cluster lainnya.

# In[45]:


# Membuat dataframe scaled
df_scaled = pd.DataFrame(df_scaled, columns = df1.columns)


# In[46]:


# mengecek dataframe
df_scaled.head()


# In[47]:


df_scaled.shape


# Untuk menentukan nilai k dalam klustering, kita akan menggunakan Elbow method. Elbow method adalah metoda yang sering dipakai untuk menentukan jumlah cluster yang akan digunakan pada k-means clustering. Tujuannya adalah menghitung WCSS se-minimum dengan jumlah cluster yang kecil agar bisa dilakukan interpretasi data.

# In[48]:


num_clusers = list(range(1,11))
ssd = []
for clustuer in num_clusers:
    kmeans = KMeans(n_clusters=clustuer, max_iter= 50)
    kmeans.fit(df_scaled)
    ssd.append(kmeans.inertia_)


# In[49]:


# Plotting metode elbow
plt.figure(figsize=(10,6))
plt.plot(num_clusers,ssd, marker = 'o')
plt.title('Elbow Method', fontsize = 16)
plt.xlabel('Number of clusters',fontsize=12)
plt.ylabel('Sum of Squared distance',fontsize=12)
plt.vlines(x=3, ymax=ssd[-1], ymin=ssd[0], colors="r", linestyles="-")
plt.hlines(y=ssd[2], xmax=9, xmin=1, colors="r", linestyles="--")

plt.show()


# Berdasarkan elbow method, kita dapat menggunakan nilai k=3

# In[50]:


# K-Mean dengan nilai k =3
kmeans = KMeans(n_clusters = 3, max_iter = 50, random_state= 50)
kmeans.fit(df_scaled)


# In[51]:


# menambahkan kolom dengan nilai hasil klustering
df_country = df.copy()
df_country['KMean_clusterid']= pd.Series(kmeans.labels_)
df_country.head()


# In[52]:


# kita akan melihat nilai masing-masing value
df_country.KMean_clusterid.value_counts()


# In[53]:


# Kita akan melakukan beberapa visualisasi dengan scatter plot menggunakan kolom dari dataset dengan korelasi yang tinggi

plt.figure(figsize=(18, 5))
plt.subplot(1, 3, 1)
sns.scatterplot(x='GDPperkapita', y='Kematian_anak', hue='KMean_clusterid', data=df_country, palette="bright", alpha=.4)

plt.subplot(1, 3, 2)
sns.scatterplot(x='Pendapatan', y='Kematian_anak', hue='KMean_clusterid',data=df_country, palette="bright", alpha=.4)

plt.subplot(1, 3, 3)
sns.scatterplot(x='GDPperkapita', y='Pendapatan', hue='KMean_clusterid', data=df_country, palette="bright", alpha=.4)

plt.show()


# In[56]:


# kita cek rata-rata mean
df_country_analysis = df_country.groupby(['KMean_clusterid']).mean().sort_values(['Kematian_anak','Pendapatan','GDPperkapita'],ascending = [False,True,True])
df_country_analysis


# berdasarkan nilai mean yang kita peroleh, didapatkan hasil klustering
# 
# - cluster 0 : Negara Berkembang
# - Cluster 1: Negara Maju
# - Cluste 2: Negara Tertinggal
# ---

# Berdasarkan hasil klustering kita bisa mendapatkan daftar 46 negara yang termasuk dalam katagori teringgal

# In[61]:


Negara_tertinggal = df_country[df_country['KMean_clusterid']== 2]
Negara_tertinggal


# Selanjutnya, kita akan memilih 5 negara paling tertinggal berdasarkan GDPperkapita, pendapatan, dan tingkat kematian anak

# In[57]:


# Memilih 5 negara paling tertinggal berdasarkan GDPperkapita, pendapatan, dan tingkat kematian anak
K_cluster_Undeveloped = df_country[df_country['KMean_clusterid']== 2]
K_top5 = K_cluster_Undeveloped.sort_values(by = ['GDPperkapita','Pendapatan','Kematian_anak'],
                                                     ascending=[True, True, False]).head(5)

print( '5 Negara paling membutuhkan bantuan:' , K_top5['Negara'].values )


# In[62]:


#Rincian 5 negara paling membutuhkan bantuan
K_top5

