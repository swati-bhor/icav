from __main__ import app
from flask import Flask, request,Response,json
import pandas as pd
from response_utils import ResponseUtil
import logging

class requestdata():
    df = pd.DataFrame()
    df = pd.read_csv('books.csv')

    @app.route('/requestdata',methods=['POST'])
    def request_data():
        try:
            json_data=request.get_json(force=True)
            row=json_data['row']
            extract_df= requestdata.df.iloc[0:row+1,:]
       
            if len(extract_df)!=0:
                data = extract_df.to_dict('r')
                return ResponseUtil("success",200).json_data_response("books",data)
            else:
                return ResponseUtil('failure',502).json_message_response('Please enter proper row number')
            
                
        except Exception as e:
            logging.error("Erro occured {}".format(e))
            return ResponseUtil('failure',403).json_message_response('Error occured while fetching the {}'.format(e))

    @app.route('/fetch_author_book', methods=['GET'])
    def fetch_author_book():
        
    
        try:
            json_data=request.get_json(force=True)
            author=json_data['author']
            extract_df = requestdata.df[requestdata.df['author']==author]
            # extract_df= requestdata.df.iloc[0:3,:]
       
            if len(extract_df)!=0:
                data = extract_df.to_dict('r')
                return ResponseUtil("success",200).json_data_response("authors",data)
            else:
                return ResponseUtil('failure',502).json_message_response('Author does not exist')
            
                
        except Exception as e:
            logging.error("Erro occured {}".format(e))
            return ResponseUtil('failure',403).json_message_response('Error occured while fetching {}'.format(e))

