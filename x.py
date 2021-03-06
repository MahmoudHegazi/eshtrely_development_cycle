﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
import os
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from werkzeug.utils import secure_filename
from flask import send_from_directory
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import TypeDecorator, Unicode
from xdb import Base, User, Sheet, History 
from flask import session as login_session
import random
import string
import excel
import httplib2
import json
from flask import make_response
import requests
import pandas as pd
from tablib import Dataset
import numpy as np
import excel
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import xlsxwriter
import pyarabic.araby as araby
import pyarabic.number as number
import arabic_reshaper
from bidi.algorithm import get_display
import sys
from sqlalchemy import func

reload(sys)  
sys.setdefaultencoding('utf-8')
engine = create_engine('sqlite:///x.db')
Base.metadata.bind = engine
engine.text_factory = str

DBSession = sessionmaker(bind=engine)
session = DBSession()

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['xls', 'xlsb', 'xlsm', 'xlsx', 'xlt', 'xltx', 'xlw', 'csv'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




class CoerceUTF8(TypeDecorator):
    """Safely coerce Python bytestrings to Unicode
    before passing off to the database."""

    impl = Unicode

    def process_bind_param(self, value, dialect):
        if isinstance(value, str):
            value = value.decode('utf-8')
        return value


@app.route('/sheet/JSON')
def sheetJSON():
    sheet = session.query(Sheet).all()
    return jsonify(Request=[r.serialize for r in sheet])



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/upload', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
	
        
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            file_path = UPLOAD_FOLDER + "/" + filename
            nx = pd.read_excel(file_path, charset='utf-8')
            lf = pd.DataFrame(nx)

            table_names = []
			# this to use arbaic and arabic libr 
            ar_request_date = u'تاريخ الطلب'
            ar_item_name = u'اسم الصنف'
            ar_description = u'المواصفات'
            ar_project = u'اسم العميل/المشروع'            
            ar_manufacturing_order = u'امر التصنيع'
            ar_order_number = u'رقم طلب المشتريات'
            ar_pr = u'pr'
            ar_unit = u'الوحدة'
            ar_quantity_to_buy = u'الكمية المطلوب شرائها'
            ar_accepted = u'الكمية المقبولة'
            ar_remaining = u'الكمية المتبقية'
            ar_delivery_date = u'تاريخ التسليم الفعلي'
            ar_supplier = u'اسم المورد'
            ar_delivery_order_number = u'رقم اذن التسليم'
            ar_notes = u'ملحظات'            
            # store all headers (columns) in one list 
            sheet_headers = [ar_request_date, ar_item_name, ar_description,
                             ar_project, ar_manufacturing_order, ar_order_number,
                             ar_pr, ar_unit, ar_quantity_to_buy, ar_accepted,
                             ar_remaining, ar_delivery_date, ar_supplier,
                             ar_delivery_order_number, ar_notes]
            #ar_request_date
            ar_item_name.encode('utf8')
            ar_description.encode('utf8')
            ar_project.encode('utf8')
            ar_manufacturing_order.encode('utf8')
            ar_order_number.encode('utf8')
            ar_pr.encode('utf8')
            ar_unit.encode('utf8')
            ar_quantity_to_buy.encode('utf8')
            ar_accepted.encode('utf8')
            ar_remaining.encode('utf8')
            ar_delivery_date.encode('utf8')
            ar_supplier.encode('utf8')
            ar_delivery_order_number.encode('utf8')
            ar_notes.encode('utf8')
            
            df = pd.DataFrame(nx, columns= sheet_headers)

            request_dates = []
            item_names = []
            descriptions = []
            projects = []
            manufacturing_orders = []
            order_numbers = []
            prs = []
            units = []
            quantitys_to_buys = []
            accepteds = []
            remainings = []
            delivery_dates = []
            suppliers = []
            delivery_orders_numbers = []
            notess = []

            #bidi_text.encode('utf8')
            for r_date in df[ar_request_date]:
                request_dates.append(str(r_date))
                print(r_date)
                
            for r_name in df[ar_item_name]:
                item_names.append(r_name)
                
            for r_description in df[ar_description]: 
                descriptions.append(r_description)
                
            for r_projet in df[ar_project]:
                projects.append(r_projet)
                
            for r_manufacturing in df[ar_manufacturing_order]:
                manufacturing_orders.append(r_manufacturing)
                
            for r_ordernumber in df[ar_order_number]:
                order_numbers.append(r_ordernumber)
                
            for r_pr in df[ar_pr]:
                prs.append(r_pr)
                
            for r_unit in df[ar_unit]:
                units.append(r_unit)
                
            for r_bquantity in df[ar_quantity_to_buy]:
                quantitys_to_buys.append(r_bquantity)
                
            for r_accepted in df[ar_accepted]:
                accepteds.append(r_accepted)
                
            for r_remaining in df[ar_remaining]:
                remainings.append(r_remaining)
                
            for r_delivery_date in df[ar_delivery_date]:
                delivery_dates.append(r_delivery_date)
                
            for r_supplier in df[ar_supplier]:
                suppliers.append(r_supplier)
                
            for r_deliver_orders in df[ar_delivery_order_number]:
                delivery_orders_numbers.append(r_deliver_orders)
                
            for r_notes in df[ar_notes]:
                notess.append(r_notes)                
            print(len(item_names))
            for row in range(len(item_names)):
                ju_request_dates = request_dates[row]
                ju_item_names = item_names[row]
                ju_descriptions = descriptions[row]
                ju_projects = projects[row]
                ju_manufacturing_orders = manufacturing_orders[row]
                ju_order_numbers = order_numbers[row]
                ju_prs = prs[row]
                ju_units = units[row]
                ju_quantitys_to_buys = quantitys_to_buys[row]
                ju_accepteds = accepteds[row]
                ju_remainings = remainings[row]
                ju_delivery_dates = delivery_dates[row]
                ju_suppliers = suppliers[row]
                ju_delivery_orders_numbers = delivery_orders_numbers[row]
                ju_notess = notess[row]
                new_row = Sheet(request_date=ju_request_dates, item_name=ju_item_names, description=ju_descriptions,
                                project=ju_projects, manufacturing_order=ju_manufacturing_orders, order_number=ju_order_numbers,
                                pr=ju_prs, unit=ju_units, quantity_to_buy=ju_quantitys_to_buys,
                                accepted=ju_accepteds, remaining=ju_remainings, delivery_date=ju_delivery_dates,
                                supplier=ju_suppliers, delivery_order_number=ju_delivery_orders_numbers, notes=ju_notess)
                session.add(new_row)
            session.commit()
            
            print("GoodJob Robot %s" % new_row.request_date)

    sheets = session.query(Sheet).order_by(asc(Sheet.id))
    return render_template('pages/forms/i_general.html')
    #sheets_number = len(session.query(Sheet).order_by(asc(Sheet.id)).all())
    #return render_template('pages/forms/i_general.html', sheets=sheets, sheets_number=sheets_number)

	


@app.route('/i_request' , methods = ['GET'])
def i_request_Function():
    return render_template('/pages/tables/i_request.html')

@app.route('/i_general', methods = ['GET'])
def ilovepython():
    return render_template('/pages/forms/i_general.html')
 
    
@app.route('/home/<int:sheet_id>' , methods=['GET', 'POST'])
def getSheet(sheet_id):
    sheet = session.query(Sheet).filter_by(id=sheet_id).first()
    page = "<style>table {width:100%;}table, th, td {border: 1px solid black;border-collapse: collapse;}th, td {  padding: 15px;text-align: left;}#t01 tr:nth-child(even) {background-color: #eee;}#t01 tr:nth-child(odd) {background-color: #fff;}#t01 th { background-color: black;color: white;}</style>"
    page += "<table><tr><th>Name</th><th>Age</th><th>Gender</th><th>phone</th><th>count</th></tr><tr>"
    page += "<td>" + str(sheet.name) + "</td>" +  "<td>" + str(sheet.pr) + "</td>" + "<td>" + str(sheet.date) + "</td>"
    page += "<td>" + str(sheet.supplier) + "</td>" + "<td>" + str(sheet.quait) + "</td></tr></table>"
    return page


@app.route('/home/all' , methods=['GET'])
def getAll():
    sheet = session.query(Sheet).all()
    page = "<style>table {width:100%;}table, th, td {border: 1px solid black;border-collapse: collapse;}th, td {  padding: 15px;text-align: left;}#t01 tr:nth-child(even) {background-color: #eee;}#t01 tr:nth-child(odd) {background-color: #fff;}#t01 th { background-color: black;color: white;}</style>"
    page += "<table><tr><th>Name</th><th>Age</th><th>Gender</th><th>phone</th><th>count</th></tr><tr>"
    for i in sheet:
        page += "<td>" + str(i.name) + "</td>" +  "<td>" + str(i.pr) + "</td>" + "<td>" + str(i.date) + "</td>"
        page += "<td>" + str(i.supplier) + "</td>" + "<td>" + str(i.quait) + "</td></tr>"
    page += "</table>"    
    return page

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
    
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8080, threaded=False)
