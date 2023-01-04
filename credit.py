import pickle
import numpy
import streamlit as st

#loading model
loaded_model=pickle.load(open("D:/model_deployment/creditmodel.sav","rb"))
def credit_predict(input_data):
    pre=loaded_model.predict(input_data)
    if(pre==[0]):
       return ("TRANSICTION IS LEGIT")
    else:
        return ("TRANSICTION IS FRAUD")
def main():
     #giving a title
            st.title("CREDIT CARD FRAUD DETECTION  WEB APP BY ANIRUDH SHARMA")
            
            v1=st.text_input("enter encoded value" ,key='1') 
            v2=st.text_input("enter encoded value" , key='2') 
            v3=st.text_input("enter encoded value", key='3') 
            v4=st.text_input("enter encoded value",key='4') 
            v5=st.text_input("enter encoded value",key='5') 
            v6=st.text_input("enter encoded value" ,key='6') 
            v7=st.text_input("enter encoded value" ,key='7') 
            v8=st.text_input("enter encoded value" ,key='8') 
            v9=st.text_input("enter encoded value", key='9') 
            v10=st.text_input("enter encoded value", key='10') 
            v11=st.text_input("enter encoded value", key='11') 
            v12=st.text_input("enter encoded value" ,key='12') 
            v13=st.text_input("enter encoded value" ,key='13') 
            v14=st.text_input("enter encoded value", key='14') 
            v15=st.text_input("enter encoded value", key='15') 
            v16=st.text_input("enter encoded value", key='16') 
            v17=st.text_input("enter encoded value", key='17') 
            v18=st.text_input("enter encoded value", key='18') 
            v19=st.text_input("enter encoded value", key='19') 
            v20=st.text_input("enter encoded value", key='20') 
            v21=st.text_input("enter encoded value", key='21') 
            v22=st.text_input("enter encoded value", key='22') 
            v23=st.text_input("enter encoded value", key='23' )
            v24=st.text_input("enter encoded value", key='24') 
            v25=st.text_input("enter encoded value", key='25') 
            v26=st.text_input("enter encoded value", key='26') 
            v27=st.text_input("enter encoded value", key='27') 
            v28=st.text_input("enter encoded value", key='28') 
            v29=st.text_input("enter encoded value", key='29') 
            v30=st.text_input("enter encoded value", key='30') 
            l=[[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29,v30]]
            
            #prediction
            result=""
            if st.button("ANALYSIS TEST RESULT"):
                 result=credit_predict(l)
            
            st.success(result)
            st.write("Thanks for your visit")
if __name__=='__main__':
     main()            
       
     
            
            