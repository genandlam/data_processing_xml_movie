#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 11:02:02 2018

@author: genevieve
"""

import xml.etree.ElementTree as ET
import os

tree = ET.parse("/Users/genevieve/Documents/MovieDiC_V2.xml")
root = tree.getroot()

# open a file for writing




#movie_data = open('/tmp/MovieDiC_V2.txt', 'w')



#printing child attrib movie
#for child in root:
#    print(child.tag, child.attrib)

# "./movie[@id='1']"

vulgar_words =['fuck!','WTF','wtf','fucking','cunt', 'fuckery','cunt','shit',"motherfuckin'",'bastard','fucker.'
               'bastard!','cunt','fucked', 'shit','fucking?','fucking',"motherfucker's",'motherfucker','Fuck',
               'fuck?!','idiot',"fuckin'","Fuckin'",'cunt!','fucker','hell',"wife-fuckin'",'fucked!','Motherfucker',
               'fuckhead','cunting','motherfucker','fuck.','fuck,','fuck','FUCKED','fuckers.','wft?','fuck?"'
               'Christ','fuckerable.','fuckerable','nigger','ass','fuckface?''fuckface!','fuckface','Fuck!','blowjob,',
               'FUCK','Jesus!','Jesus','fucks','son-of-a-bitch','bitch','bitch!','cunt.','cunt!',"cunt's",'cunt-hair',
               'cunt,','CUNT.','CUNT?!!','cunt.','Cunt!','Cunt.','cunt-rag','cunt?','bitch...','bitches.','bitch?'
               'bitch!','sonofabitch.','bitch-box.','sonofabitch','sonofabitch!','Sonofabitch','Bitch!','Bitch.',
               'bastards','assholes,','asshole.','Assholes!','dick','dickhead.','dick!','Dickhead!','dickweed',
               'dicks','cocksucker...','cocksucker',"cocksucker's",'cocksuckers!','cocksucking','cocksucker.',
               'Jackass!','jackass!','jackass','Jackass.','Jackasses.','pussy',"pussy's",'pussy!''Tit-Fucking',
               'Cock','Cum','Slut','Cocks','Blowjobs','Sucking','blowjob.','blowjob?','blowjob','tits?','Tit','tits.',
               'tits','cocksucker.','clit.','clitoris.','clitoris?','clitoris',"'clitoris'",'Clitors"!','clitoris?!',
               'boobs','boobs','cockblocking','damned','DAMN','goddamit!','Goddamnit!','Damn','damn','Goddamn','goddamn',
               'damnit','damn!','damn.','Damn,','jesus','dickless.','dickbrain','dickbrain,''dickbrain.','dickforbrains',
               'dickforbrains,','dickforbrains.','dickforbrains!','dickhead,', 'dickhead!','dickhead.','dickweed?','dickweed.',
               'dickweed!','Dickweed','dickwad','dickwad.','Dickwad.','dumb','Dumbass','dumb,'
               
               ]



count =1
while(count<616):
    file_name='movie'+str(count)+'.txt'
    location=os.path.join('/Users/genevieve/Documents/tmp/',file_name)
    f = open(location, 'wr')
    
    for dialogue in root.findall('./movie[@id="'+str(count)+'"]/dialogue'):
#    for dialogue in root.findall('./movie[@id="'+'615'+'"]/dialogue'):    
        speaker=dialogue.findall('speaker')
        
        utterance=dialogue.findall('utterance')
        speaker_list=[]
        
        for row_num in range(0,len(speaker)):
           check='' 
           utter=[]
           
           utter=[w for w in (utterance[row_num].text.lower().split()) if not w in vulgar_words]    
           utter = ' '.join((utter)).encode('utf-8').strip()
           if  row_num==0:
               speaker_list.append(speaker[row_num].text)  
               speaker1=speaker_list[0]
              
               
               f.write("speaker1: %s \n" % (utter))
#               print("speaker1: %s %s " % (speaker_list[0],utter))
               
           if row_num!=0:    
               for row in range(0,len(speaker_list)):
                   speaker1=speaker[row_num].text 
                   
                   if speaker[row_num].text ==speaker_list[row]:
                       check='yes'
                       f.write("speaker%d: %s\n"%(row+1,utter))
#                       print("speaker%d: %s %s"%(row+1,speaker_list[row],utter))
                       
               if  row==(len(speaker_list)-1) and speaker_list[row]!=speaker[row_num].text and check=='':
                   
                   speaker_list.append(speaker[row_num].text)
#                   f.write("speaker%d: %s\n"%(row+2,utter))  
 #                  print("speaker%d: %s %s"%(row+2,speaker[row_num].text,utter)) 
        
#        f.write('\n')
  #      print('\n')
    f.close()    
    count+=1
     
    
#    for speaker in speaker1:
#        speakers.append(speaker.text)
#    for utter in utterance:
#        utters.append(utter.text)
    
#    speaker1=dialogue.findall('speaker').text
#    speaker.append(speaker1)
#    utterance=dialogue.find('utterance').text
#    speaker.append(utterance)

#            
#           
#            
            
    

    
    