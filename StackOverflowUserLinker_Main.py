# -*- coding: utf-8 -*-

import sys
import urllib2
import os
import json
import gzip
import time
import pyqtgraph as pg
import random #for Testing Plots
from PIL import Image
import StringIO
from PyQt4 import QtCore, QtGui
from PyQt4.Qt import QApplication
import ui_SOUL
import ui_WidgetItemQuestion
import ui_WidgetSingleQuestion
import ui_WidgetAnswer
import ui_WidgetComment
import ui_User_Data_Dialog
import ui_WidgetUser
#import JSON_Exples


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s



#To compensate for StackExchange API reply.
true  = True
false = False

Testing = False

class UserData(object):
    def __init__(self, owner):
        self.user_id = None
        self.user_name = None
        self.owner = owner
        self.user_profile_downloaded = False
        self.user_profile_image_downloaded = False
        
class base_Class(object):
    def __init__(self, gender):
        self.author = None
        self.id = None
        self.body = None
        self.score = None
        self.link = None
        self.creation_date = None
        self.last_activity_date = None
        self.site = None
        self.gender = gender
        self.api_parameters = {'order':'desc', 'sort':'activity', 'page':1, 'page_size':100, 'site':self.site, 'intitle':'', \
                  'inname':'', 'id':'', 'action':{'type':'', 'TO':'', }}
        
    #def build_API_Url(self, question_id=0, api_site='stackoverflow', page=1, page_size=30, order='desc', sort='activity'):
    def build_API_Url(self, **kwargs):        

        filter_question = '&filter=!*af)D9PEgGZbY2ji39oRqs39tTAIjjwxiX(_Npg0K2(nVx)gQwVTC4Nm.(ZeFjcF*hV1a_4F2q2couV30Vm'
        base_url = 'http://api.stackexchange.com/2.2'
        
        if self.gender=='Q':
            '''Question related API'''
            if kwargs['action']['type']=='GET':
                #GET Question Details
                return base_url + '/questions/' + str(kwargs['id']) + '?order=' + kwargs['order'] + '&sort=' + kwargs['sort'] + \
                    '&site=' + kwargs['site'] + '&page=' + str(kwargs['page']) + '&pagesize=' + str(kwargs['page_size']) + \
                    filter_question
                    
            elif kwargs['action']['type']=='POST':                
                if kwargs['action']['TO']=='ANSWER':
                    pass
                    
                elif kwargs['action']['TO']=='COMMENT':
                    pass
                
                elif kwargs['action']['TO']=='FLAG':
                    pass
            
                elif kwargs['action']['TO']=='VOTE_UP':
                    pass
                
                elif kwargs['action']['TO']=='VOTE_DOWN':
                    pass
                
                elif kwargs['action']['TO']=='EDIT':
                    pass
            
        elif self.gender=='A':
            '''Answer related API'''
            if type['action']['type']=='GET':
                pass
            
            elif kwargs['action']['type']=='POST':                    
                if kwargs['action']['TO']=='COMMENT':
                    pass
                
                elif kwargs['action']['TO']=='FLAG':
                    pass
            
                elif kwargs['action']['TO']=='VOTE_UP':
                    pass
                
                elif kwargs['action']['TO']=='VOTE_DOWN':
                    pass
                
                elif kwargs['action']['TO']=='EDIT':
                    pass
            
        elif self.gender=='C':
            '''Comment related API'''
            if type['action']['type']=='GET':
                pass
            
            elif kwargs['action']['type']=='POST':                  
                if kwargs['action']['TO']=='FLAG':
                    pass
            
                elif kwargs['action']['TO']=='VOTE_UP':
                    pass
            
        #add elif cases for up/down voting, comments, answers, flags, .... etc
            
     
    
    def post_Url(self):
        
        api_url = self.build_API_Url(self.api_parameters)
            
        
        print 'Retrieving from: \n', api_url
        #self.label_Dialog_Status.setText('Downloading User %d API data from %s...' %(self.user.user_id, url))
        try:
            req = urllib2.Request(api_url, headers={'Accept-Encoding':'gzip'})
            resp = urllib2.urlopen(req).read()
        except Exception as e:
            print e
            #print e.reason
            #print e.msg
            return None
        buff = StringIO.StringIO(resp)
        zip_data = gzip.GzipFile(fileobj=buff)
        data = json.loads(zip_data.read())
        #self.label_Dialog_Status.setText('User %d API data successfully downloadd' % self.user.user_id)
        #save data into Json File
        return data
    
    def retrieve_Data(self):
        pass
        
        
    def vote(self, up=True, undo=False):
        pass
    
    def comment_post(self, delete=False):
        pass
        
    def flag(self):
        pass
    
    def favortie(self):
        pass

class question(base_Class):    
    
    def __init__(self):
        super(question, self).__init__('Q')
        self.site = None
        self.comments_count = None
        self.comments_list = []
        self.answers_count = None
        self.answers_list = []
        self.accepted_answer = None
        self.retrieve_Data()
        
        #self.comments_list = [comment() for c in range(self.comments_count) if self.comments_count]
        '''
        if self.comments_count:
            for c in range(self.comments_count):
                self.comment = comment()
                self.comments_list.append(self.comment)
        '''     
        #self.answers_list = [answer() for a in range(self.answers_count) if self.answers_count]  
            
        '''
        if self.answers_count: 
            for a in range(self.answers_count):
                self.answer = answer()
                self.answers_list.append(self.answer)
        '''
            
        

                                         
        
        
    def retrieve_Data(self):
        data = self.download_API()
        if data['total'] == 0:
            return None
        '''
      "tags": [
        "javascript",
        "python",
        "arrays",
        "django",
        "templates"
      ],
      "owner": {
        "badge_counts": {
          "bronze": 5,
          "silver": 0,
          "gold": 0
        },
        "reputation": 30,
        "user_id": 4454084,
        "user_type": "registered",
        "accept_rate": 40,
        "profile_image": "https://lh3.googleusercontent.com/-Sr4LfNqoGwE/AAAAAAAAAAI/AAAAAAAAFEc/23xhrK0-pug/photo.jpg?sz=128",
        "display_name": "Sudha M.R.",
        "link": "http://stackoverflow.com/users/4454084/sudha-m-r"
      },
      "comment_count": 0,
      "view_count": 27,
      "favorite_count": 0,
      "down_vote_count": 0,
      "up_vote_count": 1,
      "accepted_answer_id": 32584774,
      "answer_count": 2,
      "score": 1,
      "last_activity_date": 1442318772,
      "creation_date": 1442315976,
      "question_id": 32584686,
      "link": "http://stackoverflow.com/questions/32584686/using-list-from-views-in-django-1-8-1-as-an-array-in-javascript-template",
      "title": "Using list from views in Django 1.8.1 as an array in javascript template",
      "body": "<p>I have a piece of code in views.py that gets the file names from a directory:</p>\n\n<pre><code>def imgArray(request):\nfilepath = STATIC_PATH+\"\\\\images\"\nimageArray=[]\next='.jpg'\nfor i in os.listdir(filepath):\n    if(os.path.splitext(i)[1] == ext):      \n         imageArray.append( i )\ncontext = {'imageArray': imageArray}\nprint context\nreturn render(request, 'imgpage/add_category.html',context)\n\n\n\ndef add_category(request):\n    # A HTTP POST?\n    if request.method == 'POST':\n       #Do some actions\n    else:\n        # If the request was not a POST, display the form to enter details.\n        imageArray = imgArray(request)\n    return render(request, 'imgpage/add_category.html')\n</code></pre>\n\n<p>I want to use this array of image files in javascript. I want to use the array of file names so that I can use js to change image source.\nThe <code>print context</code> statement yields the following output in the python console:</p>\n\n<pre><code>{'imageArray': ['image0.jpg', 'image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.\njpg', 'image5.jpg', 'image6.jpg', 'image7.jpg', 'image8.jpg', 'image9.jpg']}\n</code></pre>\n\n<p>But I am not able to access the imageArray at all in the template. Here are the scripts I tried to test if the array has been passed, in the template html file:</p>\n\n<p>In add_category.html file:</p>\n\n<pre><code>{% for img in imageArray %}\n        &lt;li&gt;{{ img|safe }}&lt;/li&gt;\n        &lt;li&gt;{{ img }}&lt;/li&gt;\n        &lt;p&gt;img&lt;/p&gt;\n{% endfor %}\n</code></pre>\n\n<p>Also, note that the \"img\" inside <code>&lt;p&gt;</code> tags are also not rendered on the screen.</p>\n\n<pre><code>&lt;script type=\"text/javascript\"&gt;\n        var images = \"{{imageArray|safe}}\";\n        console.log(images);\n        console.log(\"imgx=\"+images[1]);\n        document.getElementsByTagName(\"img\")[0].src =  DJANGO_STATIC_URL+images[2];\n    &lt;/script&gt;\n</code></pre>\n\n<p>In the above script, the first console log prints empty line in the console, while the 2nd prints \"imgx=undefined\"</p>\n\n<p>Please suggest me ways I can use the python list as JS array. I use Django 1.8.1, but the service I would host on uses 1.7.x. So something that would work on both would be great.</p>\n"
    }
    '''
        self.author = data['items']['owner']
        self.id = data['items']['question_id']
        self.body = data['items']['body']
        #self.vote = data['items']['up_vote_count']-data['items']['down_vote_count']
        self.vote = data['items']['score']
        self.link = data['items']['link'] 
        self.creation_date = data['items']['creation_date'] 
        self.last_activity_date = data['items']['last_activity_date']
        self.site = None #Need to add it to filter
        self.comments_count = data['items']['comment_count']
        self.comments_list = []
        self.answers_count =data['items']['answer_count']
        self.answers_list = []
        self.accepted_answer = data['items']['accepted_answer_id']
        
    
        
class answer(object, base_Class):
    def __init__(self):
        super(answer, self).__init__('A')
        
class comment(object, base_Class):
    def __init__(self):
        super(comment, self).__init__('C')
        
    
        
        
        
class SEUL(QtGui.QMainWindow, ui_SOUL.Ui_MainWindow):
    def __init__(self, parent=None):
        super(SEUL, self).__init__(parent)
        
        #########################
        #self.user_id = 1327005  #
        #self.user_id = 2867928  #
        #self.user_id = 4244780  #
        #self.user_id = 707111   #
        #self.user_id = 3297613  #
        #self.user_id = 1768232  #
        #self.user_id = 7432     #
        #self.user_id = 298479
        #self.user_id = 180784
        #self.user_id = 100297
        #########################
        self.user = UserData()
        #self.dialogCreated = False #replaced it with isinstance built-in method...if good remove this line
        self.followList = [] #list to keep track of questions to follow
        self.setupUi(self)
        self.pw = pg.PlotWidget(name='Reputation History')
        self.horizontalLayout_Plot.addWidget(self.pw)
        #self.statusbar.setText('Welcome user %d :)' % self.user.user_id)
        self.cur_dir = os.getcwd() #Need to re-check this expression
        self.connect(self.actionUser_Data, QtCore.SIGNAL('triggered()'), self.user_data_Dialog)
        settings_path = self.cur_dir + os.sep + 'settings.txt'
        if os.path.exists(settings_path): 
            self.first_time = False
            with open('settings.txt') as settings:
                id_line = settings.readline()
                self.user.user_id = int(id_line.split(': ')[1])
                name_line = settings.readline()
                self.user.user_name = name_line.split(': ')[1]
        else:
            self.first_time = True
        self.setup_User_Tab()
        self.setup_Question_Tab()
        ##user_url = self.build_Url(user_data=True)
        ##reputation_trend_url = self.build_Url(reputation_trend=True)
        ##self.plot_Reputation_History(reputation_trend_url)
        #self.user_data = data_exple #For Testing Purpose
        
        '''
        profile_data_Json_file = self.cur_dir + os.sep + self.user.user_id.__str__() + '_user_data.json'
        if (os.path.exists(profile_data_Json_file)):
            #loads user data profile from Json file
            print profile_data_Json_file
            self.load_Profile_data(profile_data_Json_file, user_url)
        else:
            #TO-DO: write a method to construct user_url depending on provided site, user_id ... etc
            self.user.user_profile_image_downloaded = False
            self.setup_new_Profile(self.user_data)
            print 'Setting up new Profile'
        '''
        
        #self.display_user_data(self.user_data['items'][0])
        
    def load_Profile_data(self, profile_path, user_url):
        print 'LOADING PROFILE'
        #loads user data from JSON file
        if Testing:
            print 'Simulating with User Data Exple...\n'
            user_data = JSON_Exples.user_data_exple
        else:
            user_data = self.retrieve_API(user_url) #Handle Case of unable to retrieve Data
        data = self.load_from_JSON(profile_path, user_Data=True)
        #print data
        #print data.__class__
        if not isinstance(data, 'String'.__class__) and user_data:
            if data['items'][0]['last_modified_date'] < user_data['items'][0]['last_modified_date']:
                self.save_as_JSON(user_data, userData=True)
                #self.label_Dialog_Status.setText('New Profile date for user %d downloaded...' % self.user.user_id)
                msg = 'New Profile date for user %d downloaded...' % self.user.user_id
                self.update_Status_Bar(msg)
            if data['items'][0]['profile_image'] != user_data['items'][0]['profile_image'] and not Testing:
                new_img_url = user_data['items'][0]['profile_image']
                self.download_Profile_Image(new_img_url)
                #self.label_Dialog_Status.setText('New Profile Image for user %d downloaded...' % self.user.user_id)
                msg = 'New Profile Image for user %d downloaded...' % self.user.user_id
                self.update_Status_Bar(msg)

        else:
            print 'NO DATA LOADED'     
            user_data = data
            #self.label_Dialog_Status.setText('User Data loaded from %s...' % profile_path)
        
        self.user.user_id = user_data['items'][0]['user_id']
        self.user.user_name = user_data['items'][0]['display_name']
        profile_image_path = self.cur_dir + os.sep + self.user.user_id.__str__() + '_profile.jpg'
        if os.path.exists(profile_image_path):
            self.user.user_profile_image_downloaded = True
        return user_data
    
    def setup_new_Profile(self, user_url):
        
        print 'NEW PROFILE'
        #1-Download API Data:
        #self.label_Dialog_Status.setText('Downloading new user %d profile data...' % self.user.user_id)
        msg = 'Downloading new user %d profile data...' % self.user.user_id
        self.update_Status_Bar(msg)
        user_data = self.retrieve_API(user_url)
        #2-Save User Data as JSON file
        self.save_as_JSON(user_data, userData=True)
        #3-Download Profile Image:
        img_url = user_data['items'][0]['profile_image']
        #self.label_Dialog_Status.setText('Downloading user %d Profile Image...' % self.user.user_id)
        self.download_Profile_Image(img_url)
        return user_data
        
    def download_Profile_Image(self, url, name=None):
        if name is None:
            name = str(self.user.user_id)
        try:    
            req = urllib2.Request(url)
            resp = urllib2.urlopen(url)
        except urllib2.URLError as e:
            print e.reason
            #self.label_Dialog_Status.setText(e.reason)
            self.user.user_profile_image_downloaded = False
        else:
            data = StringIO.StringIO(resp.read())
            img = Image.open(data)
            save_to_path = self.cur_dir+os.sep+name+'_profile.jpg'
            #print save_to_path
            img.save(save_to_path)            
            self.user.user_profile_image_downloaded = True
            #self.label_Dialog_Status.setText('Profile Image downloaded Successfuly..')
            return save_to_path
        
    def display_user_data(self, data):
        
        #1-Tab Namimg, Profile Image, Badges & Repuations
        #cur_index = self.tabWidget_Main.currentIndex()
        name = QtCore.QString(data['display_name'])
        self.tabWidget_Main.setTabText(0,name)
        img_path = str(data['user_id'])+'_profile.jpg'
        userTab_icon = QtGui.QIcon(img_path)
        self.tabWidget_Main.setTabIcon(0, userTab_icon)
        self.load_Image_Profile(img_path)        
        self.lcd_Gold.display(data['badge_counts']['gold'])   
        self.lcd_Silver.display(data['badge_counts']['silver'])  
        self.lcd_Bronze.display(data['badge_counts']['bronze']) 
        self.lcd_Repuation.display(data['reputation'])
        self.lcd_Daily_Change.display(data['reputation_change_day'])
                
        #2-Display Name
        font = self.changeFont(family='Courier', point=25, italic=True, bold=True)
        self.label_Display_Name.setFont(font)
        self.label_Display_Name.setText(QtCore.QString.fromUtf8(data['display_name']))
        
        #3-About Me
        font = self.changeFont(family='Arial', point=17, italic=True)
        #self.label_About_Me.setFont(font)
        self.textBrowser_About_Me.setFont(font)
        #self.label_About_Me.setText(QtCore.QString(data.get('about_me','No About Me text provided by user!')))
        self.textBrowser_About_Me.setText(QtCore.QString(data.get('about_me','No About Me text provided by user!')))
        #4-User Attributes
        user_attributes = ['question_count','answer_count','last_access_date','location','view_count','link','website_url']
        prefix = []
        suffix = [' Question(s) asked', ' Answer(s) posted', ' last time seen','', ' time(s) Profile viewd', '', '']
        #print data
        for attr, suf in zip(user_attributes, suffix):
            font = self.changeFont(family='Arial', point=12)
            ref = getattr(self, 'label_'+attr)
            ref.setFont(font)
            #print self.user_data['items'][0][attr]
            if attr == 'last_access_date': 
                #TO-DO: Fix This Code block
                #cur_time = time.localtime()
                #last_time = time.localtime(data[attr])
                #fields = ['tm_year', 'tm_mon', 'tm_mday', 'tm_hour', 'tm_min', 'tm_sec']
                #suf = ['year','month','day','hour','minute, second']
                #msg = ' '.join(zip([str(getattr(cur_time, f)-getattr(last_time, f)) for f in fields], suf))
                #print 'Last access date in epoch format', data[attr]
                attr = time.strftime('%a, %d %b %Y %H:%M:%S', time.localtime(data[attr]))
                #print 'Last access date in humain format', attr
                ref.setText(attr+suf)
                #ref.setText('Last seen %s ago' % time.strftime('%a, %d %b %Y %H:%M:%S', time.localtime(data[attr])))
                #ref.setText(msg)
            if attr == 'location':
                myLocation = data.get(attr, 'Unknown')
                ref.setText(myLocation)
                if myLocation is not 'Unknown':
                    flag_path = os.getcwd()+os.sep+'flags'
                    #print flag_path
                    for flag in os.listdir(flag_path):
                        #print flag
                        #flag = unicode(flag)
                        flag = flag.decode('utf-8')
                        if flag[:-4].replace('_',' ') in myLocation:
                            flag_profile = QtGui.QImage(flag_path+os.sep+flag)
                            self.label_Flag.setPixmap(QtGui.QPixmap.fromImage(flag_profile))                
                          
                
                
            else:
                #ref.setText(''.join((str(data.get('attr',None)),suf)))
                ref.setText(str(data.get(attr,None))+suf)
                
    def setup_User_Tab(self): 
        #TO-DO: Doc String to write
        '''
        user_attributes = ['Gold_Badge','Silver_Badge','Bronze_Badge','question_count','answer_count','last_access_date','location','view_count','link','website_url','reputation','reputation_change_day']
        for attr in user_attributes:
            img = QtGui.QImage(self.cur_dir+os.sep+attr+'.png')
            ref = getattr(self, 'label_'+attr+'_icon')
            ref.setPixmap(QtGui.QPixmap.fromImage(img))
        '''    
        if self.first_time:
            #print 'Calling User Dialog'
            self.user_data_Dialog()
            self.save_Settings()
        user_url = self.build_Url(user_data=True)
        reputation_trend_url = self.build_Url(reputation_trend=True)
        profile_data_Json_file = self.cur_dir + os.sep + self.user.user_id.__str__() + '_user_data.json'
        if (os.path.exists(profile_data_Json_file)):
            #loads user data profile from Json file
            print 'Loading Profile Data from %s' % profile_data_Json_file
            msg = 'loading user %d profile data from %s...' %(self.user.user_id, profile_data_Json_file)
            self.update_Status_Bar(msg)
            user_data = self.load_Profile_data(profile_data_Json_file, user_url)
        else:
            #TO-DO: write a method to construct user_url depending on provided site, user_id ... etc
            #self.user.user_profile_image_downloaded = False
            #self.label_Dialog_Status.setText('Setting up new user %d profile data' %self.user.user_id)
            msg = 'Setting up new user %d profile data' % self.user.user_id
            self.update_Status_Bar(msg)
            user_data = self.setup_new_Profile(user_url)
            print 'Setting up new Profile'
         
        #Display User Profile
        #print 'Data to Display:\n', self.user_data['items'][0]
        self.display_user_data(user_data['items'][0]) 
        ##self.plot_Reputation_History(reputation_trend_url) #Commented for testing purposes
          
    def load_Image_Profile(self, image_path=None):
        if not self.user.user_profile_image_downloaded:
            self.label_Profile_Image.setText('Couldn\'t download Profile Image..')
        else:
            self.image_profile = QtGui.QImage(image_path) #TODO - STREAM IMAGE DATA DIRECTLY TO LABEL_PROFILE_IMAGE without saving it, but think of drawbacks (everytime need to download)
            self.image_profile = self.image_profile.scaled(250,250, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
            self.label_Profile_Image.setPixmap(QtGui.QPixmap.fromImage(self.image_profile))                
   
    def build_Url(self, question_id=0, answer_id=0, user_id=0, name='Khalil', user_data=False, reputation_trend=False, question=False, tags=False, sites=False, \
                  answers_details=False, comments=False,  favorite=False, users=False, api_site='stackoverflow', tag='python', page=1, page_size=30, \
                  order='desc', sort='activity'):
        
        filter_user = '&filter=8G3NojNB'
        filter_reputation = '&filter=!40)4tHeU_N6aXv)dv'
        filter_question = '&filter=!*IXs7G1IOvdNDZLb8WU1)UaETlUbGWbi-Nri6pAi4T5xT_uL*p)B)mk(Z5Fzk-'
        filter_sites = '&filter=!)Qpa1bGM8FLSKXcD_xvK6ksE'
        filter_tags = '&filter=!-*f(6tFG3.5M'
        filter_answers = '&filter=!gmIHlYkBRyzXi)EKnPEyg_c2UUk-hSUnGkm'
        filter_comments = '&filter=!)Q2ANGPUEPdbOVxmAJ_Ybhwj'
        filter_favorite = '&filter=!)5IW-5QuertpO1qS82WOJpak_-NU'
        filter_users = '&filter=.OjDlwF-0efNZParv12h4'
        base_url = 'http://api.stackexchange.com/2.2'
        #base_url = 'http://api.stackexchange.com/2.2/users/1327005?site=stackoverflow&filter=8G3NojNB'    
        #reputation_trend_url = 'http://api.stackexchange.com/2.2/users/1327005/reputation?page=1&pagesize=100&site=stackoverflow&filter=!40)4tHeU_N6aXv)dv'

        if user_data:
            return base_url + '/users/' + self.user.user_id.__str__() + '?site=' + api_site + filter_user
        
        elif reputation_trend:
            return base_url + '/users/' + self.user.user_id.__str__() + '/reputation?site=' + api_site +'&page=' + str(page) + \
                   '&pagesize=' + str(page_size) + filter_reputation
        elif question:
            return base_url + '/questions?order='+order+'&sort='+sort+'&site=' + api_site + '&tagged=' + tag + \
                '&page=' + str(page) + '&pagesize=' + str(page_size) + filter_question 
        elif tags:
            return base_url + '/tags?order='+order+'&sort='+sort+'&site=' + api_site +'&page=' + str(page) + \
                   '&pagesize=' + str(page_size) + filter_tags
        elif sites:
            return base_url + '/sites?page='+str(page) + '&pagesize=' + str(page_size) + filter_sites
        
        elif answers_details:
            return base_url + '/questions/' + str(question_id) + '/answers?order=' + order + '&sort=' + sort + '&site=' + api_site + \
                   '&page=' + str(page) + '&pagesize=' + str(page_size) + filter_answers
            
        elif comments:
            if question_id:
                return base_url + '/questions/' + str(question_id) + '/comments?order=' + order + '&sort=' + sort + '&site=' + api_site + \
                   '&page=' + str(page) + '&pagesize=' + str(page_size) + filter_comments
            elif answer_id:
                return base_url + '/answers/' + str(answer_id) + '/comments?order=' + order + '&sort=' + sort + '&site=' + api_site + \
                   '&page=' + str(page) + '&pagesize=' + str(page_size) + filter_comments
        
        elif favorite:
            return base_url + '/users/' + str(self.user.user_id) + '/favorites?order=' + order + '&sort=' + sort + '&site=' + api_site + \
                   '&page=' + str(page) + '&pagesize=' + str(page_size) + filter_favorite
                    
        elif users:
            if user_id != 0:
                #https://api.stackexchange.com/2.2/users/1327005?page=1&pagesize=100&order=desc&sort=name&site=stackoverflow&filter=!LnNkvq16GJcA8z0KCPgxcz
                return base_url + '/users/' + str(user_id) + '?order=' + order + '&sort=' + sort + '&site=' + api_site + \
                   '&page=' + str(page) + '&pagesize=' + str(page_size) + filter_users
            else:
                #/2.2/users?order=desc&sort=reputation&inname=khalil&site=stackoverflow&filter=!)RwcIFLf9ZNmSBc4if75mxYI
                name = name.replace(' ', '%20')
                return base_url + '/users?' + 'order=' + order + '&sort=' + sort + '&inname=' + name + '&site=' + api_site + \
                       '&page=' + str(page) + '&pagesize=' + str(page_size) + filter_users
                       
    def retrieve_API(self, url): 
        print 'Retrieving from: \n', url
        #self.label_Dialog_Status.setText('Downloading User %d API data from %s...' %(self.user.user_id, url))
        try:
            req = urllib2.Request(url, headers={'Accept-Encoding':'gzip'})
            resp = urllib2.urlopen(req).read()
        except Exception as e:
            print e
            #print e.reason
            #print e.msg
            return None
        buff = StringIO.StringIO(resp)
        zip_data = gzip.GzipFile(fileobj=buff)
        data = json.loads(zip_data.read())
        #self.label_Dialog_Status.setText('User %d API data successfully downloadd' % self.user.user_id)
        #save data into Json File
        return data
    
    def plot_Reputation_History(self,url):
        #TO-DO: This method does not full data and get key_error exception, blocks app_launching as it keeps downloading and parsing plot data
        #Convert it to a Thread, Might generalize it to downloading it user profile as a separate Thread to not block application from Lauchinhg and wait for data retrieval.
        #For this method specificaly better parse each retrieved page and save data into a JSON file than at the end of operation re-open file, and each time you just retrieve new data 
        #just to date where lastly retrieved.
        
        step = 1
        
        #plot = self.retrieve_API(url)
        plot_file = self.user_data['items'][0]['user_id'].__str__() + '_user_plot.json'
        #plot_data = plot['items'][-1::-step] #We don't need the whole plot data just to visualize the Trend(Repuation Summary)
        #print plot_data
        p = 2
        
        #Implement data retrieve on fromDate to toDate
        if (os.path.exists(plot_file)):
            print 'Downloading User Plot Data...'
            #self.label_Dialog_Status.setText('Loading user %d Plot Data...' % self.user.user_id)
            #save plot data(fromdate to todate) to existing Json file 
            tmp = self.load_from_JSON(plot_file, plot_Data=True, mode='r')
            #print 'Debugging tmp:\n',tmp
            plot = tmp
            plot['has_more'] = False
            fromdate = tmp['last_on_date']
            todate = int(time.time())
            if todate - fromdate > 86400: #more than a day
                #self.label_Dialog_Status.setText('Downloading new user %d Plot Data..' % self.user.user_id)
                plot = self.retrieve_API(url+'&fromdate='+fromdate.__str__()+'&todate='+todate.__str__())
                #print 'Plot:\n', plot
                if plot is not None and plot['items']:
                    #print 'Plot data:\n', plot
                    plot_data = plot['items'][0::step] #We don't need the whole plot data just to visualize the Trend(Repuation Summary)
                    tmp['items'].extend(plot_data)
                    #tmp['last_on_date'] = sorted(plot_data, key=lambda s: s['on_date'])[-1]['on_date']
                    #print plot_data
                    tmp['last_on_date'] = plot_data[0]['on_date']
                    if not plot['has_more']:
                        tmp['items'] = sorted(tmp['items'], key=lambda s:s['on_date'])
                        self.save_as_JSON(tmp, user_plot=True, mode='w')
                        #print 'from if block:\n', tmp
                    
                    #/2.2/users/4244780/reputation?page=1&pagesize=100&fromdate=1438387200&todate=1440460800&site=stackoverflow&filter=!40)4tHeU_N6aXv)dv
                '''
                else:
                    plot = tmp
                    plot['has_more'] = False
                #print 'Plot :\n', plot
                '''
        else:
            #save plot data to new file as 'user_id_user_plot.json'
            plot = self.retrieve_API(url)
            #print 'Plot:\n', plot
            if plot is None:
                print 'No Plot Data could be retrieved'
                return 
            #print 'from Else Block:\n',plot
            plot_data = plot['items'][0::step]
            #last_time = sorted(plot_data, key=lambda s: s['on_date'])[0]['on_date']
            last_time = plot_data[0]['on_date']
            tmp = {'last_on_date':last_time, 'items':plot_data}
            if not plot['has_more']:
                tmp['items'] = sorted(tmp['items'], key=lambda s:s['on_date'])
                self.save_as_JSON(tmp, user_plot=True, mode='w')
                
        #if more data to retrieve, then:   
        while plot['has_more']:
            #print 'Next page..'
            url = url.replace('page='+str(p-1),'page='+str(p))
            #print url
            plot = self.retrieve_API(url)
            plot_data = plot['items'][0::step]
            #tmp = self.load_from_JSON(plot_file, plot_Data=True, mode='r')
            #print 'From while loop:\n',tmp
            tmp['items'].extend(plot_data)
            #tmp['last_on_date'] = sorted(plot_data, key=lambda s: s['on_date'])[-1]['on_date']
            #print 'Next Data:\n'
            #print plot_data
            if not plot['has_more']:
                tmp['items'] = sorted(tmp['items'], key=lambda s:s['on_date'])
                self.save_as_JSON(tmp, user_plot=True, mode='w')
                break
            else:
                p += 1
                continue
                    
        #data = sorted(plot_data, key=lambda s:s['on_date'])
        #print data
        #TO-DO: Fix X-axis to display Human Time Stamp instead of Epoch Time Stamp
        #x = [tmp['items'][i]['on_date'] for i in range(len(tmp['items']))]
        #y = [tmp['items'][i]['reputation_change'] for i in range(len(tmp['items']))]
        
        #tmp = self.load_from_JSON(plot_file, plot_Data=True, mode='r')
        #print tmp
        coord = [elem.values() for elem in tmp['items'] if len(elem) > 1]
        #print coord
        #Need to think about sorting!
        #y = sorted(y)
        #x = sorted(x)
        #x.reverse()
        #y.reverse()
        x = [elem[0] for elem in coord]
        y = [elem[1] for elem in coord]
        #print x 
        #print y
        y = [sum(y[0:i+1]) for i in range(len(y))]
        #print y
        self.pw.plot(x,y)
        
    def save_as_JSON(self, data, settings=False, questions=False, userData=False, user_plot=False, mode='w', sort=False):
        #id = self.user_data['items'][0]['user_id']
        id = data['items'][0]['user_id']
        timestamp = time.strftime('%a, %d %b %Y %H:%M:%S', time.localtime())
        if settings:
            pass
        elif questions:
            pass
        elif userData:
            user_file_path = self.cur_dir + os.sep + id.__str__() + '_user_data.json'
            with open(user_file_path, mode) as fp:
                data['Date'] = timestamp
                json.dump(data, fp, default=timestamp, indent=4)
        elif user_plot:
            user_plot_file = self.cur_dir + os.sep + id.__str__() + '_user_plot.json'
            #last_date_on = data[]
            with open(user_plot_file, mode) as fp:
                json.dump(data, fp, default=timestamp, indent=4, sort_keys=sort)
        
    
    def load_from_JSON(self, json_file, settings=False, questions=False, user_Data=False, plot_Data = False, mode='r'):
        if settings:
            pass
        elif questions:
            pass
        elif user_Data or plot_Data:
            try:
                with open(json_file, mode) as fp:
                    data = json.load(fp)
                
            except Exception as e:
                print e
                print 'No %s file found!' %json_file
                return 'NO DATA'   
            return data
        
    def changeFont(self, family=None, point=-1, weight=-1, italic=False, bold=False, line_spacing=1, cap_style=QtGui.QFont.MixedCase):
        font = QtGui.QFont(family, point, weight, italic)
        if point > 0:
            font.setPointSize(point)
        if bold:
            font.setBold(True)
        font.setCapitalization(cap_style)
        font.setFamily('Arial')  
        return font  
    
    def setup_Question_Tab(self):
        
        sites_url = self.build_Url(sites=True, page_size=100)
        print 'Sites URL = %s' % sites_url
        if Testing:
            print 'Simulating with Sites Exple...\n'
            sites_list = JSON_Exples.sites_exple
        else:
            sites_list = self.retrieve_API(sites_url)
        self.d_name_to_api = {}
        for item in sites_list['items']:
            self.tq_comboBox_Sites.addItem(QtCore.QString(item['name']))
            self.d_name_to_api[item['name']]=item['api_site_parameter']
        self.connect(self.tq_comboBox_Sites, QtCore.SIGNAL('currentIndexChanged (const QString&)'), self.update_Tag)
        print 'Dictionay:\n', self.d_name_to_api    
        site_selected = str(self.tq_comboBox_Sites.currentText())  
        print 'Site selected: ',site_selected
        tag_url = self.build_Url(tags=True, api_site=self.d_name_to_api[site_selected])
        print 'Tag URL = %s' % tag_url
        if Testing:
            print 'Simulating with Programmers Tags Exple...\n'
            tag_list = JSON_Exples.tags_Programmers_exple
        else:
            tag_list = self.retrieve_API(tag_url)
        for item in tag_list['items']:
            self.tq_comboBox_Tags.addItem(QtCore.QString(item['name']))
            
        
            
        sort_list = ['activity', 'votes', 'creation', 'hot', 'week', 'month']
        for item in sort_list:
            self.tq_comboBox_Sort.addItem(QtCore.QString(item))
            
        order_list = ['desc', 'asc']
        for item in order_list:
            self.tq_comboBox_Order.addItem(QtCore.QString(item))
            
        #self.query_Question()
        self.connect(self.tq_pushButton_Query, QtCore.SIGNAL('clicked()'), self.query_Question) 

    def query_Question(self):
        pageSize = self.tq_lineEdit_PageSize.text()
        pageNb = self.tq_lineEdit_PabeNb.text()
        tag = str(self.tq_comboBox_Tags.currentText()) #Need to convert QString to str
        order = str(self.tq_comboBox_Order.currentText()) #Need to convert QString to str
        sort = str(self.tq_comboBox_Sort.currentText()) #Need to convert QString to str
        site = str(self.tq_comboBox_Sites.currentText())
        #print 'TAGS = ', tag, pageNb, pageSize
        if len(pageSize):
            pageSize = int(pageSize)
        else:
            pageSize = 50
        if len(pageNb):
            pageNb = int(pageNb)
        else:
            pageNb = 1
        #question_url += '&tagged='+tag+'&order='+order+'&sort='+sort
        #question_url = 'http://api.stackexchange.com/2.2/questions?pagesize=10&order=desc&sort=activity&tagged=python&site=stackoverflow&filter=!m)Bb_U8PAXUva4(RraE9GMvhhBdolt1Q9On(2oq9a(*Ut6man*KqHAfI'
        question_url = self.build_Url(api_site=self.d_name_to_api[site], page=pageNb, page_size=pageSize, sort=sort, order=order, question=True, tag=tag)
        print 'Question URL = %s' % question_url
        if Testing:
            print 'Simulating with Questions Exple...\n'
            q_list = JSON_Exples.question_exple
        else:
            q_list = self.retrieve_API(question_url)
        #print 'q_list:'
        #print q_list
        self.listWidget_Questions.clear()
        for i,item in enumerate(q_list['items']):
            print item
            q_item = QtGui.QListWidgetItem(self.listWidget_Questions)
            q_item.setSizeHint(QtCore.QSize(830,100))
            self.listWidget_Questions.addItem(q_item)
            question_item = ui_WidgetItemQuestion.Ui_FORM()
            question_item.setupUi(self)
            question_item.wq_label_Title.setText(item['title'][:60] + '...')
            #question_item.wq_label_Title.setObjectName(question_item.wq_label_Title.objectName+item['question_id'].__str__())
            self.connect(question_item.wq_label_Title, QtCore.SIGNAL('clicked()'), lambda q_id=item['question_id'], \
                         q_item=item: self.get_Answers_Details(q_id,self.d_name_to_api[site],q_item))
            question_item.wq_label_Author.setText('asked by '+item['owner']['display_name'])
            question_item.wq_label_body.setText(item['body'][:80] + '...')
            question_item.wq_label_answers.setText(str(item.get('answer_count','0'))+' answers')
            question_item.wq_label_votes.setText(str(item.get('up_vote_count','0')+item.get('down_vote_count','0'))+' votes')
            question_item.wq_label_comments.setText(str(item.get('comment_count','0'))+' comments')
            question_item.wq_label_views.setText(str(item.get('view_count','0'))+' views')
            icon_path = os.getcwd()+os.sep+'site_icons'+os.sep+site+'.png'
            #print icon_path
            question_icon = QtGui.QImage(icon_path) #TODO - STREAM IMAGE DATA DIRECTLY TO LABEL_PROFILE_IMAGE without saving it, but think of drawbacks (everytime need to download)
            question_item.wq_label_Site.setPixmap(QtGui.QPixmap.fromImage(question_icon))
            if item['is_answered']:
                question_state_path = os.getcwd() + os.sep + 'answered_48x48.png'
            else:
                question_state_path = os.getcwd() + os.sep + 'unanswered_48x48.png'               
            question_state_icon = QtGui.QImage(question_state_path)
            question_item.wq_label_Question_State.setPixmap(QtGui.QPixmap.fromImage(question_state_icon))                
   
            self.listWidget_Questions.setItemWidget(q_item, question_item.wq_Frame)
        
    def update_Tag(self, current_Site):
        print 'Site has changed, updating Tag list'
        self.tq_comboBox_Tags.clear()
        current_Site = self.d_name_to_api[str(current_Site)]
        tag_url = self.build_Url(tags=True, api_site=current_Site)
        print 'Updated Tag URL = %s' % tag_url
        tag_list = self.retrieve_API(tag_url)
        for item in tag_list['items']:
            self.tq_comboBox_Tags.addItem(QtCore.QString(item['name']))
                
    
    def get_Answers_Details(self, q_id, site, question_item):
        print 'Question Title Clicked @ %d' % q_id  
        answers_details_url = self.build_Url(answers_details=True, question_id=q_id, api_site=site, page_size=10)
        print 'Question details URL = %s' % answers_details_url
        if Testing:
            print 'Simulating with Single Question Exple...\n'
            answers_list = JSON_Exples.question_details_exple
        else:
            answers_list = self.retrieve_API(answers_details_url)
        #print question_details_list
        #print 'Question:\n',question_item
        comments_url = self.build_Url(question_id=q_id,comments=True, api_site=site, page_size=10, sort='creation')
        print 'Comments URL = %s' % comments_url
        if Testing:
            print 'Simulating with Question Comments Exple...\n'
            comments_list = JSON_Exples.question_comments_exple
        else:
            comments_list = self.retrieve_API(comments_url)
        self.setup_Up_Question_Tab('Question',site)
        answers_count = self.setup_Up_Question_Details_Widget(question_item, comments_list)
        if answers_count:
            for i,item in enumerate(answers_list['items']):
                self.setup_Up_Answer_Widget(item, site,i)
                        
        '''
        q_item = QtGui.QListWidgetItem(self.tsq_listWidget)
        q_item.setSizeHint(QtCore.QSize(995,910))
        self.tsq_listWidget.addItem(q_item)
        question_item = ui_SingleQuestion.Ui_Form()
        question_item.setupUi(self)
        self.tsq_listWidget.setItemWidget(q_item, question_item.tsq_frame_Question)
        
        q_item = QtGui.QListWidgetItem(self.tsq_listWidget)
        q_item.setSizeHint(QtCore.QSize(995,910))
        self.tsq_listWidget.addItem(q_item)
        question_item = ui_SingleAnswer.Ui_Form()
        question_item.setupUi(self)
        self.tsq_listWidget.setItemWidget(q_item, question_item.tsq_frame_Answer)
        
        q_item = QtGui.QListWidgetItem(self.tsq_listWidget)
        q_item.setSizeHint(QtCore.QSize(995,910))
        self.tsq_listWidget.addItem(q_item)
        question_item = ui_SingleAnswer.Ui_Form()
        question_item.setupUi(self)
        self.tsq_listWidget.setItemWidget(q_item, question_item.tsq_frame_Answer)
        '''
    
    def setup_Up_Question_Details_Widget(self, q_details, c_list):
        print q_details
        q_item = QtGui.QListWidgetItem(self.tsq_listWidget)
        q_item.setSizeHint(QtCore.QSize(995,910))
        self.tsq_listWidget.addItem(q_item)
        question_item = ui_WidgetSingleQuestion.Ui_Form()
        question_item.setupUi(self.tsq_listWidget)
        question_item.tsq_label_Question_Title.setText(q_details['title'])
        #body_size = self.calculate_body_size(q_details['body'])
        #print 'Body Size = %d' % body_size
        #question_item.tsq_textBrowser_Question_Body.setMinimumHeight(body_size)
        question_item.tsq_textBrowser_Question_Body.setText(q_details['body'])
        print 'Question Body Height = ', question_item.tsq_textBrowser_Question_Body.document().size()
        question_item.tsq_label_Question_Owner_Name.setText('asked by '+q_details['owner']['display_name']+' @ Some Time')
        question_item.tsq_label_Question_Owner_Repuation.setText(str(q_details['owner']['reputation']))
        question_item.tsq_label_Question_Owner_Gold.setText(str(q_details['owner'].get('badge_counts',0)['gold']))
        question_item.tsq_label_Question_Owner_Silver.setText(str(q_details['owner'].get('badge_counts',0)['silver']))
        question_item.tsq_label_Question_Owner_Bronze.setText(str(q_details['owner'].get('badge_counts',0)['bronze']))
        #icon_path = self.download_Profile_Image(q_details['owner']['profile_image'], str(q_details['owner']['user_id']))
        #print icon_path
        #question_icon = QtGui.QImage(icon_path) #TODO - STREAM IMAGE DATA DIRECTLY TO LABEL_PROFILE_IMAGE without saving it, but think of drawbacks (everytime need to download)
        #question_icon.scaled(48, 48)
        #question_item.tsq_label_Question_Owner_Profile.setPixmap(QtGui.QPixmap.fromImage(question_icon))
        question_item.tsq_label_Question_Score.setText(str(q_details['score']))
        
        if q_details['comment_count'] < 5:
            question_item.tsq_listWidget_Question_Comments.setFixedSize(QtCore.QSize(920,q_details['comment_count']*50))
        else:
            question_item.tsq_listWidget_Question_Comments.setFixedSize(QtCore.QSize(920,200))
        
        question_item.tsq_label_Answer_Count.setText(str(q_details['answer_count'])+' Answer(s) posted')
        #question_item.wq_label_answers.setText(str(q_details.get('answer_count','0'))+' answers')
        #question_item.wq_label_votes.setText(str(q_details.get('up_vote_count','0')+q_details.get('down_vote_count','0'))+' votes')
        #question_item.wq_label_comments.setText(str(q_details.get('comment_count','0'))+' comments')
        #question_item.wq_label_views.setText(str(q_details.get('view_count','0'))+' views')     
        self.tsq_listWidget.setItemWidget(q_item, question_item.tsq_frame_Question)
        #print 'Total Comments = ', c_list['total']
        #print 'Range = ', range(c_list['total'])
        #print 'Length of items = ', len(c_list['items'])
        for i in range(len(c_list['items'])):
            self.setup_Up_Comment_Widget(question_item.tsq_listWidget_Question_Comments, c_list['items'][i])
        
        
        return q_details['answer_count']
    
    def calculate_body_size(self, text):
        new_lines = text.count('\n')
        line_size = len(text)/80
        return new_lines+line_size
        
    def setup_Up_Comment_Widget(self, list_Widget, item):
        c_item = QtGui.QListWidgetItem(list_Widget)
        c_item.setSizeHint(QtCore.QSize(918,50))
        #c_item.setSizeHint(QtCore.QSize(list_Widget.width,50))
        list_Widget.addItem(c_item)
        comment_item = ui_WidgetComment.Ui_Form()
        comment_item.setupUi(list_Widget)
        comment_item.tsq_label_Comment_Score.setText(str(item['score']))
        comment_item.tsq_textBrowser_Comment_Body.setText(item['body'])
        comment_item.tsq_label_Comment_Author.setText(item['owner']['display_name'])
        list_Widget.setItemWidget(c_item, comment_item.tsq_frame_Comment)
        
        
    def setup_Up_Answer_Widget(self, item, site,i):
        a_item = QtGui.QListWidgetItem(self.tsq_listWidget)
        a_item.setSizeHint(QtCore.QSize(995,910))
        self.tsq_listWidget.addItem(a_item)
        answer_item = ui_WidgetAnswer.Ui_Form()
        answer_item.setupUi(self.tsq_listWidget)
        answer_item.tsq_textBrowser_Answer_Body.setText(item['body'])
        h = answer_item.tsq_textBrowser_Answer_Body.document().size().height()
        print 'Answer Body Height = ', h
        if h < answer_item.tsq_textBrowser_Answer_Body.sizeHint().height():
            answer_item.tsq_textBrowser_Answer_Body.setMinimumHeight(h)
            answer_item.tsq_textBrowser_Answer_Body.updateGeometry()
        answer_item.tsq_label_Answer_Owner_Name.setText(item['owner']['display_name'])
        answer_item.tsq_label_Answer_Owner_Repuation.setText(str(item['owner']['reputation']))
        answer_item.tsq_label_Answer_Owner_Gold.setText(str(item['owner'].get('badge_counts',0)['gold']))
        answer_item.tsq_label_Answer_Owner_Silver.setText(str(item['owner'].get('badge_counts',0)['silver']))
        answer_item.tsq_label_Answer_Owner_Bronze.setText(str(item['owner'].get('badge_counts',0)['bronze']))
        answer_item.tsq_label_Answer_Score.setText(str(item['score']))
        #icon_path = self.download_Profile_Image(item['owner']['profile_image'], str(item['owner']['user_id']))
        #print icon_path
        #answer_icon = QtGui.QImage(icon_path) #TODO - STREAM IMAGE DATA DIRECTLY TO LABEL_PROFILE_IMAGE without saving it, but think of drawbacks (everytime need to download)
        #answer_icon.scaled(answer_item.tsq_label_Answer_Owner_Profile.size())
        #answer_item.tsq_label_Answer_Owner_Profile.setPixmap(QtGui.QPixmap.fromImage(answer_icon))
        if item['is_accepted']:
                answer_accepted_path = os.getcwd() + os.sep + 'answered_48x48.png'
                answer_accepted_icon = QtGui.QImage(answer_accepted_path)
                answer_item.tsq_label_Answer_Accepted.setPixmap(QtGui.QPixmap.fromImage(answer_accepted_icon))     
        self.tsq_listWidget.setItemWidget(a_item, answer_item.tsq_frame_Answer)
        
        comments_url = self.build_Url(answer_id=item['answer_id'],comments=True, api_site=site, page_size=10, sort='creation')
        print comments_url
        if Testing:
            #JSON_Exples.answer1_comments_exple
            print 'Simulating with Answer Comments Exple...\n'
            comments_list = getattr(JSON_Exples,'answer'+str(i)+'_comments_exple')
        else:
            comments_list = self.retrieve_API(comments_url)
        if len(comments_list['items']) < 5:
            answer_item.tsq_listWidget_Answer_Comments.setFixedSize(QtCore.QSize(920,len(comments_list['items'])*50))
        else:
            answer_item.tsq_listWidget_Answer_Comments.setFixedSize(QtCore.QSize(920,4*50))#max of four comments view in listWidget
        
        for i in range(len(comments_list['items'])):
            self.setup_Up_Comment_Widget(answer_item.tsq_listWidget_Answer_Comments, comments_list['items'][i])


    def setup_Up_Question_Tab(self, name, site):
        self.tab_question_details = QtGui.QWidget()
        self.tab_question_details.setObjectName(_fromUtf8('question_details'))        
        #self.horizontalLayout_list = QtGui.QHBoxLayout(self.tab_question_details)
        #self.horizontalLayout_list.setSpacing(5)
        #self.horizontalLayout_list.setContentsMargins(0, 0, 0, 0)
        #self.horizontalLayout_list.setObjectName(_fromUtf8("horizontalLayout_list"))
        self.tabWidget_Main.setTabText(self.tabWidget_Main.indexOf(self.tab_question_details),name)
        self.horizontalLayout_16 = QtGui.QHBoxLayout(self.tab_question_details)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setMargin(0)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.tsq_listWidget = QtGui.QListWidget(self.tab_question_details)
        #self.tsq_listWidget.setTextElideMode(QtCore.Qt.ElideRight)
        #self.tsq_listWidget.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        #self.tsq_listWidget.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        #self.tsq_listWidget.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(98, 98, 98, 255), stop:1 rgba(199, 199, 199, 255));"))
        #self.tsq_listWidget.setStyleSheet(_fromUtf8("background-color: rgb(80, 80, 80);"))
        #self.tsq_listWidget.setStyleSheet(_fromUtf8("background-color: rgb(97, 48, 72);"))
        self.tsq_listWidget.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(92, 13, 52, 255), stop:1 rgba(203, 121, 96, 255));\n"
                                                    "border-color: rgba(255, 255, 255, 0);"))

        self.tsq_listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #self.tsq_listWidget.setAutoScroll(False)
        self.tsq_listWidget.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tsq_listWidget.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tsq_listWidget.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tsq_listWidget.setMovement(QtGui.QListView.Free)
        #self.tsq_listWidget.setResizeMode(QtGui.QListView.Adjust)
        self.tsq_listWidget.setUniformItemSizes(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.tsq_listWidget.setSizePolicy(sizePolicy)   
        #self.horizontalLayout_list.addItem(self.tsq_listWidget)     
        self.tsq_listWidget.setObjectName(_fromUtf8("tsq_listWidget"))
        self.horizontalLayout_16.addWidget(self.tsq_listWidget)
        self.tabWidget_Main.addTab(self.tab_question_details, _fromUtf8(name))
        icon_path = os.getcwd()+os.sep+'site_icons'+os.sep+site+'.png'
        userTab_icon = QtGui.QIcon(icon_path)
        self.tabWidget_Main.setTabIcon(self.tabWidget_Main.indexOf(self.tab_question_details), userTab_icon)  
        #self.tab_question_details.setFocus()
        #self.tabWidget_Main.currentIndex() 
        
    def user_data_Dialog(self):
        #if self.dialogCreated:
        if isinstance(self.dialog_User_Data, QtGui.QDialog):
            self.dialog_User_Data.show()
        else:
            #self.dialogCreated = True            
            dialog = ui_User_Data_Dialog.Ui_dialog_User_Data()
            self.dialog_User_Data = QtGui.QDialog(self)
            dialog.setupUi(self.dialog_User_Data)
            #dialog.listWidget__Dialog_User_data_Users
            #test = self.list_Users(list_Widget=dialog.listWidget__Dialog_User_data_Users)
            self.connect(dialog.pushButton_Dialog_User_Data_Lookup, QtCore.SIGNAL('clicked()'), \
                         lambda d=dialog: self.list_Users(d))
            self.connect(dialog.checkBox_Widget_User_Data_Show_Password, QtCore.SIGNAL('stateChanged(int)'), lambda s=dialog.checkBox_Widget_User_Data_Show_Password.checkState(), d=dialog: self.setPasswordMask(s,d))
            self.connect(dialog.textEdit_Dialog_User_data_Listing, QtCore.SIGNAL('textChanged()'), dialog.textEdit_Dialog_User_data_Listing.repaint)
            
            if self.dialog_User_Data.exec_():
                '''
                new_user_id = dialog.lineEdit__Dialog_User_data_User_ID.text().toInt()[0]
                print new_user_id
                if not self.user.user_id and new_user_id != self.user.user_id:
                    self.user.user_id = new_user_id
                    msg = 'User ID Changed from %d to %d ...' %(self.user.user_id, new_user_id)
                    self.update_Status_Bar(msg)
                '''
                pass
            
            
    def update_Status_Bar(self, msg):
        self.statusBar().showMessage(msg, 10000)
        
    def list_Users(self, dialog):      
        #self.update_Status_Bar(msg)
        if dialog.lineEdit__Dialog_User_data_User_ID.text():
            print 'Using User ID'
            ID = dialog.lineEdit__Dialog_User_data_User_ID.text().toInt()[0]
            users_url = self.build_Url(user_id=ID, users=True, api_site='stackoverflow', page_size=100, sort='reputation')
        elif dialog.lineEdit_Dialog_User_data_User_Name.text():
            name = str(dialog.lineEdit_Dialog_User_data_User_Name.text())
            users_url = self.build_Url(users=True, api_site='stackoverflow', page_size=100, sort='reputation', name=name)
        print users_url
        dialog.textEdit_Dialog_User_data_Listing.clear()
        dialog.textEdit_Dialog_User_data_Listing.setText('Contacting Server...')
        dialog.textEdit_Dialog_User_data_Listing.repaint()
        cursor = dialog.textEdit_Dialog_User_data_Listing.textCursor()
        cursor.movePosition(QtGui.QTextCursor.EndOfLine, QtGui.QTextCursor.MoveAnchor);
        cursor.insertText('[OK]')
        dialog.textEdit_Dialog_User_data_Listing.append('Retrieving Users Data...')
        #print 'Cursor at :', cursor.position()
        #print 'Cursor at :', cursor.positionInBlock()
        #print 'Cursor at :', cursor.anchor()
        users = self.retrieve_API(users_url)
        cursor.movePosition(QtGui.QTextCursor.EndOfLine, QtGui.QTextCursor.MoveAnchor);
        cursor.insertText('[OK]')
        #time.sleep(10)
        #print users
        dialog.listWidget__Dialog_User_data_Users.clear()
        for i in range(users['total']):
            myFrame = QtGui.QFrame()
            u_item = QtGui.QListWidgetItem(dialog.listWidget__Dialog_User_data_Users)
            u_item.setSizeHint(QtCore.QSize(152,120))
            dialog.listWidget__Dialog_User_data_Users.addItem(u_item)
            user_item = ui_WidgetUser.Ui_Frame_Widget_User()
            user_item.setupUi(myFrame)
            user = users['items'][i]
            user_item.label_Widget_User_Repuation.setText(users['items'][i]['reputation'].__str__())
            user_item.label_Widget_User_Name.setText(users['items'][i]['display_name'])
            user_item.label_Widget_User_Gold.setText(users['items'][i]['badge_counts']['gold'].__str__())
            user_item.label_Widget_User_Silver.setText(users['items'][i]['badge_counts']['silver'].__str__())
            user_item.label_Widget_User_Bronze.setText(users['items'][i]['badge_counts']['bronze'].__str__())
            self.connect(user_item.label_Widget_User_Name, QtCore.SIGNAL('clicked()'), lambda u=user, d=dialog: self.select_User(u,d))
            dialog.listWidget__Dialog_User_data_Users.setItemWidget(u_item, user_item.Widget_Widget_User)
    
        u_item = QtGui.QListWidgetItem(dialog.listWidget__Dialog_User_data_Users)
        u_item.setSizeHint(QtCore.QSize(152,120))
        dialog.listWidget__Dialog_User_data_Users.addItem(u_item)
        
        
        

            
    def setPasswordMask(self, state, dialog):
        if state == QtCore.Qt.Unchecked:
            print 'Not Checked'  
            dialog.lineEdit_Dialog_User_data_Password.setEchoMode(QtGui.QLineEdit.Normal) 
        elif state == QtCore.Qt.Checked:
            print 'Checked'     
            dialog.lineEdit_Dialog_User_data_Password.setEchoMode(QtGui.QLineEdit.Password) 
    
    def select_User(self, user, dialog):
        dialog.lineEdit__Dialog_User_data_User_ID.setText(user['user_id'].__str__())
        self.user.user_id = user['user_id']    
        dialog.lineEdit_Dialog_User_data_User_Name.setText(user['display_name'])
        self.user.user_name = user['display_name']
        if self.user.user_id and user['user_id'] != self.user.user_id:
            msg = 'User ID Changed from %d to %d ...' %(self.user.user_id, user['user_id'])
            self.update_Status_Bar(msg)
            dialog.textEdit_Dialog_User_data_Listing.append('User ID Changed from %d to %d ...' %(self.user.user_id, user['user_id']))
        elif not self.user.user_id:
            msg = 'New User ID %d ...' % self.user.user_id
            self.update_Status_Bar(msg)
            dialog.textEdit_Dialog_User_data_Listing.append('New User ID %d ...' % self.user.user_id)
        self.setup_User_Tab()
        
    def save_Settings(self):
        settings_path = self.cur_dir + os.sep + 'settings.txt'
        with open('settings.txt', 'w') as settings:
            id_line = 'User ID: ' + self.user.user_id.__str__() + '\n'
            settings.write(id_line)
            name_line = 'User Name: ' + self.user.user_name + '\n'
            settings.write(name_line)
            
app = QApplication(sys.argv)        
myApp =SEUL()
print 'Returned from __init__'
myApp.show()
app.exec_()
