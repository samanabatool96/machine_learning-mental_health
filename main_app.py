from seaborn.palettes import color_palette
from All_files import *
from All_files import MultiApp
from apps import analysis_app,extract_app,user_app

app=MultiApp()
with open("styles/style.css") as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
side_bar=st.beta_container()
col1, mid, col2 = st.beta_columns([2,1,20])
with col1:
    st.image('images/circle-cropped.png', width=80)
with col2:
    st.markdown("<h1 style='text-align:center;font-weight:bolder;font-size:89px; color: #356E98;  font-family: 	Copperplate'>You Are <br><br>What <br><br>You Tweet</h1>", unsafe_allow_html=True) 
with side_bar:
    st.sidebar.image("images/Logo_v.png", width=250)

menu = ["Home","How it Works","Learn","Main Analysis"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.markdown('#') 
    """
    Every life is believed to be like a light and every life that goes out much too soon is previous. We lost many great people due to suicide and this alarming and needs to be changed.It is mandatory to find out people who are suffering and this is considered to be the first phase that is this whole project is based on.
    """
    st.markdown('##') 
    data=load_file("./datasets/who_suicide_statistics.csv")
    st.title('## Distribution of suicides from the year 1985 to 2016')
    fig = plt.figure(figsize=(20, 10))
    ax = plt.axes()
    ax.tick_params(axis='x', colors='white')   
    ax.tick_params(axis='y', colors='white')
    ax.set_facecolor("#0D0F12")
    fig.patch.set_facecolor('xkcd:black')
    data['year'].value_counts(normalize = True )
    data['year'].value_counts(dropna = False).plot.bar(color = 'blue', figsize = (8, 6))


    plt.xlabel('year',color="white")
    plt.ylabel('count',color="white")
    st.pyplot(fig)
    





    


elif choice == "How it Works":
    """
    ## Steps
    1. **Extract Tweets**- creating tweet dataset for analysis if you do not have a dataset.
    2. **Analyse Tweets** - creating a tweet analysis report for English or German.
    ***After usage check off the used check box proceeding with the next operation***
    
    """ 

elif choice == "Learn":
    """
    # Machine Learning And Mental Health
    ### DATA that will talk to you if you're willing to Listen.
    """
    st.write(
        """
           Web-scrapping and Data Analytics falls under my project domain. Web scraping, web mining, or web harvesting are data mining techniques that collect or extract large amounts of data from various websites or social media. It is usually accomplished using scripts that interface with web through browser or direct protocols like html etc. The ‘scrapped’ or extracted data is pre-processed and archived as structured or unstructured database. We intend using Twitter as data source and Twitter APIs for extracting the data.  
           Data Analytics is a wild field encompassing various techniques. Under the project we intend using Natural Language Processing (NLP) and Machine Learning (ML) to classify the tweets as per the mood and emotion.  
        """
    )
elif choice =="Main Analysis":
    st.title("Twitter Analytics option")
    app.add_app("Extract Tweets",extract_app.app)
    app.add_app("Analysis Datasets",analysis_app.app)
    app.add_app("User Analysis",user_app.app)
    
    app.run()

     