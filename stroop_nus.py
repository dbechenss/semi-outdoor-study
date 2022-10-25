# -*- coding: utf-8 -*-
researchinfo="""
Software Development of Stroop Color and Word Test

The ability to inhabit cognitive interference can be measured by formula : 
total time + 2 * mean time per word * number of uncorrected errors (Stroop, 1935)
where, total time is the overall time for reading; mean time per word 
is the overall time for reading divided by the number of items; and 
the number of uncorrected errors is the number of errors not spontaneously corrected.

Default settings:
Congruent trials: 20
Incongruent trials: 20

Corresponding author: Chen Shisheng(chenshisheng@u.nus.edu)
"""



licen="""
   Copyright © 2020 Chen Shisheng & He Yang

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
   
  Apache License
  Version 2.0, January 2704
  http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS
"""
import tkinter  
from tkinter import *
import tkinter.scrolledtext as st
import random
import os 
import pandas as pd
import time
from time import localtime, strftime




class myWindow:
    def __init__(self, root, flag, password):
        if password=='000000':        
            self.top = tkinter.Toplevel(root, width=700, height=600)
            self.top.geometry("600x600")
            self.top.resizable(width=False, height=False)
            self.top.title('Stroop Color and Word Test')
            self.top.attributes('-topmost', 1)
            
            if flag==1:
                
                global testdate
                global types, words, colors, answers, duration
                
                testdate=strftime("%Y%m%d_%H%M", localtime()) #for xls file
                
                
                #define congruent
                def congruent():
                    tot = ['Red', 'Blue', 'Green', 'Yellow']
                    word_s = random.choice(tot)
                    words.append(word_s)
                    colors.append(word_s)
                    types.append('congruent')
                    return (word_s, word_s)
                #define incongruent
                def incongruent():
                    tot = ['Red', 'Blue', 'Green', 'Yellow']
                    word_s = random.choice(tot)
                    tot.remove(word_s)
                    color_s = random.choice(tot)
                    words.append(word_s)
                    colors.append(color_s)
                    types.append('incongruent')
                    return (word_s, color_s)
    
                def stroop():
                    tot = ['Red', 'Blue', 'Green', 'Yellow']
                    word_s = random.choice(tot)
                    
                    if random.choice((True, False))==True:
                        words.append(word_s)
                        colors.append(word_s)
                        return (word_s, word_s)
                    else:
                        tot.remove(word_s)
                        color_s = random.choice(tot)
                        words.append(word_s)
                        colors.append(color_s)
                        return (word_s, color_s)
            
                def next_stroop():
                    #global sequence of strooplist
                    global a, st, df_score
                    #evaluation ui with df score
                    if a > len(strooplist) -1:
                        #label.config(text='End of test', fg='red',font=50)
                        label.config(text=' \n'+'End of test', fg='red',font=('Times New Roman',30), bg='lightgray')
                        label.update()
                        time.sleep(2)
                        self.top.destroy()
                        
                        # text=tkinter.Text(upframe, height=8, width=30, font=20)
                        # textstr=df_score.set_index('total_time').T
                        # text.insert(INSERT, str(textstr))
                        # text.pack()
                        #self.top.destroy()
                    else:
                        if strooplist[a] == 'congru':
                            word, color = congruent()
                        else:
                            word, color = incongruent()
                        
                        st=time.time()
                        label.config(text=' \n'+word, fg=color)
                        label.update()
                
                        #global sequence of strooplist
                        a=a+1
                
                # def congru_score():
                #     global total_time_congru, mean_time_congru, df
                #     #congruent
                #     df_congru=df.loc[(df['types']=='congruent')]
                #     total_time_congru=sum(df_congru['duration'])
                #     mean_time_congru=sum(df_congru['duration']) / len(df_congru['duration'])
                    
                #     if df_congru['evaluation'].str.contains('False').any() == True:
                #         df_congru_uncorrect=df_congru.loc[(df_congru['evaluation']=='False')]
                #         n_uncorrect_congru=df_congru_uncorrect['evaluation'].value_counts().loc['False']
                #     return (total_time_congru, mean_time_congru)
        
                # def incongru_score():
                #     global total_time_incongru, mean_time_incongru, df
                #     #incongruent
                #     df_incongru=df.loc[(df['types']=='incongruent')]
                #     total_time_incongru=sum(df_incongru['duration'])
                #     mean_time_incongru=sum(df_incongru['duration']) / len(df_incongru['duration'])
                    
                #     if df_incongru['evaluation'].str.contains('False').any() == True:
                #         df_incongru_uncorrect=df_incongru.loc[(df_incongru['evaluation']=='False')]
                #         n_uncorrect_incongru=df_incongru_uncorrect['evaluation'].value_counts().loc['False']
                        
                #     #df_incongru=df.loc[(df['evaluation']=='False')]
                #     return (total_time_incongru, mean_time_incongru)

                def data_score():
                    global df_score, total_time, mean_time, n_uncorrect, score
                    #summary of results
                    df_score=pd.DataFrame({'total_time':[round (total_time, 3)], 'mean_time':[round (mean_time, 3)], 
                    'number_uncorrect':[n_uncorrect],'overall score':[round (score, 3)], 
                    'total_time_congruent':[round (total_time_congru, 3)], 'mean_time_congruent':[round (mean_time_congru, 3)], 
                    'number_uncorrect_congru':[n_uncorrect_congru],'score_congru':[round (score_congru, 3)], 
                    'total_time_incongruent':[round (total_time_incongru, 3)],'mean_time_incongruent':[round (mean_time_incongru, 3)], 
                    'number_uncorrect_incongru':[n_uncorrect_incongru],'score_incongru':[round (score_incongru, 3)]
                    ,'interference score':[round (score_stroop, 3)],
                    'start_time': [testdate], 'user': [testor_name.get()]})
                    return df_score
                
                
                def savedata():
                    global df
                    global total_time, mean_time, n_uncorrect, score
                    global total_time_congru, mean_time_congru, n_uncorrect_congru, score_congru
                    global total_time_incongru, mean_time_incongru, n_uncorrect_incongru, score_incongru
                    global score_stroop

                   
                    df=pd.DataFrame([types, words, colors, answers, duration]).T
                    df.columns=['types', 'words', 'colors', 'answers', 'duration']
                    #evaluation of answers
                    checks=[]
                    for i in range(0, len(df)):
                        if df['colors'].iloc[i] == df['answers'].iloc[i]:
                            checks.append('True')
                        else:
                            checks.append('False')
                    df['evaluation']=pd.DataFrame(checks)
                    df=df.dropna()
                    #stroop interference score calculation
                    if len(df) == len(strooplist):
                        #overall
                        total_time=sum(df['duration'])
                        mean_time=sum(df['duration']) / len(df['duration'])
                        #congru
                        df_congru=df.loc[(df['types']=='congruent')]
                        total_time_congru=sum(df_congru['duration'])
                        mean_time_congru=sum(df_congru['duration']) / len(df_congru['duration'])
                        #incongruent
                        df_incongru=df.loc[(df['types']=='incongruent')]
                        total_time_incongru=sum(df_incongru['duration'])
                        mean_time_incongru=sum(df_incongru['duration']) / len(df_incongru['duration'])
                        
                        #count uncorrect and score
                        #s1: all false
                        if df['evaluation'].str.contains('False').all() == True:
                            n_uncorrect=df['evaluation'].value_counts().loc['False']
                            n_uncorrect_congru=df_congru['evaluation'].value_counts().loc['False']
                            n_uncorrect_incongru=df_incongru['evaluation'].value_counts().loc['False']
                            
                            score = total_time + 2*mean_time*n_uncorrect
                            score_congru = total_time_congru + 2*mean_time_congru*n_uncorrect_congru
                            score_incongru = total_time_incongru + 2*mean_time_incongru*n_uncorrect_incongru
                            score_stroop = score_incongru - score_congru
                          
                            df_score=data_score()
                        else:
                            #s2: false and true
                            if df['evaluation'].str.contains('False').any() == True:
                                n_uncorrect=df['evaluation'].value_counts().loc['False']
                                if df_congru['evaluation'].str.contains('False').any() == True:
                                    n_uncorrect_congru=df_congru['evaluation'].value_counts().loc['False']
                                else:
                                    n_uncorrect_congru=0
                                if df_incongru['evaluation'].str.contains('False').any() == True:
                                    n_uncorrect_incongru=df_incongru['evaluation'].value_counts().loc['False']
                                else:
                                    n_uncorrect_incongru=0
                                
                                score = total_time + 2*mean_time*n_uncorrect
                                score_congru = total_time_congru + 2*mean_time_congru*n_uncorrect_congru
                                score_incongru = total_time_incongru + 2*mean_time_incongru*n_uncorrect_incongru
                                score_stroop = score_incongru - score_congru
                              
                                df_score=data_score()
                            else:
                                #s3: all correct
                                # uncorrect=0
                                n_uncorrect=0
                                n_uncorrect_congru=0
                                n_uncorrect_incongru=0
                                #score =total time
                                score = total_time
                                score_congru=total_time_congru
                                score_incongru=total_time_incongru
                                score_stroop = score_incongru - score_congru
       
                                df_score=data_score()
                        df=pd.concat([df, df_score], axis=1, sort=False)
                    df.to_excel('Stroop results_'+testdate+'_'+testor_name.get()+'.xls', index=False)

                #button: append answers and duration, save data and next stroop
                def _red():
                    et=time.time()-st
                    answer='Red'
                    answers.append(answer)
                    duration.append(round(et,3))
                    savedata()
                    next_stroop()
                    
                
                def _blue():
                    et=time.time()-st
                    answer='Blue'
                    answers.append(answer)
                    duration.append(round(et,3))
                    savedata()
                    next_stroop()
                
                def _green():
                    et=time.time()-st
                    answer='Green'
                    answers.append(answer)
                    duration.append(round(et,3))
                    savedata()
                    next_stroop()
                
                def _yellow():
                    et=time.time()-st
                    answer='Yellow'
                    answers.append(answer)
                    duration.append(round(et,3))
                    savedata()
                    next_stroop()
                
                #First step of stroop test
                def run_stroop():
                    #global sequence of strooplist
                    global a
                    global st
                    #determine congru or incongru
                    if strooplist[0] == 'congru':
                        word, color = congruent()
                    else:
                        word, color = incongruent()
                        
                    st=time.time()

                    label.config(text=' \n'+word, fg=color,font=('Times New Roman',60), bg='lightgray')
                    label.update()
                    a=1

                #list to be saved   
                types=[]
                words=[]
                colors=[]
                answers=[]
                duration=[]
                
                # stroop list based on coefficient of congruent and incongruent trials
                # cof=int(sss0.get())
                # icof=int(sss1.get())
                cof=2
                icof=2
                strooplist=['congru']*cof + ['incongru']*icof
                random.shuffle(strooplist)
                

                #GUI
                upframe = Frame(self.top, bg='lightgray')
                upframe.pack(side = TOP,expand = True, fill = BOTH )
                
                bottomframe = Frame(self.top)
                bottomframe.pack( side = BOTTOM,expand = True, fill = BOTH )
                
                start = tkinter.Button(upframe, text='Start', command=run_stroop, font=('Times New Roman',20), bg='lightgray')
                start.pack(side = TOP, fill = BOTH)
                
                label = tkinter.Label(upframe, text=' \n',font=('Times New Roman',60), bg='lightgray')
                label.pack()
                
                red = tkinter.Button(bottomframe, text='Red', command=_red, font=('Times New Roman',20), bg='lightgray')
                red.pack(side = LEFT, expand = True, fill = BOTH) 
                
                blue = tkinter.Button(bottomframe, text='Blue', command=_blue, font=('Times New Roman',20), bg='lightgray')
                blue.pack(side = LEFT, expand = True, fill = BOTH) 
                
                green = tkinter.Button(bottomframe, text='Green', command=_green, font=('Times New Roman',20), bg='lightgray')
                green.pack(side = LEFT, expand = True, fill = BOTH) 
                
                yellow = tkinter.Button(bottomframe, text='Yellow', command=_yellow, font=('Times New Roman',20), bg='lightgray')
                yellow.pack(side = LEFT, expand = True, fill = BOTH) 

#For about menu
def clickabout():
    t = tkinter.Toplevel()
    t.title('Info')
    text_area = st.ScrolledText(t, font = ("Times New Roman", 12), width=85,height=18) 
    text_area.grid() 
    # Inserting Text which is read only 
    text_area.tag_configure('tag', justify='center')
    text_area.insert(tkinter.INSERT, researchinfo,'tag') 
    # Making the text read only 
    text_area.configure(state ='disabled')
    
#For license menu
def clicklicense():
    t = tkinter.Toplevel()
    t.title('License')
    # Creating scrolled text area 
    # widget with Read only by 
    # disabling the state 
    text_area = st.ScrolledText(t, font = ("Times New Roman", 10), width=85,height=50) 
    text_area.grid() 
    # Inserting Text which is read only 
    text_area.tag_configure('tag', justify='center')
    text_area.insert(tkinter.INSERT, licen,'tag') 
    # Making the text read only 
    text_area.configure(state ='disabled')

root = tkinter.Tk()
root.geometry("600x600")
root.resizable(width=False, height=False)
root.title('Stroop Color and Word Test')
root.configure(bg='lightgray')
window1 = tkinter.IntVar(root, value=0)

menubar=tkinter.Menu(root)
helpmenu=tkinter.Menu(menubar, tearoff=0)
helpmenu.add_command(label='About', command=clickabout)
helpmenu.add_command(label='License', command=clicklicense)
menubar.add_cascade(label='Help', menu=helpmenu)

#setting of entry position
h=40
w=250
xe=300
label00=tkinter.Label(root,text='Stroop Test',font=('Times New Roman',25), bg='lightgray')
label00.place(x=35, rely=0.03)
label2=tkinter.Label(root,text='Password:',font=('Times New Roman',12), bg='lightgray')
label2.place(x=35,y=100)
label3=tkinter.Label(root,text='User name:',font=('Times New Roman',12), bg='lightgray')
label3.place(x=35,y=150)
default0=tkinter.Variable()
default0.set('000000')
password=tkinter.Entry(root,text=default0)
password.place(x=xe,y=95,height=h,width=w)
default2=tkinter.Variable()
testor_name=tkinter.Entry(root,text=default2)
testor_name.place(x=xe,y=155,height=h,width=w)

# #settings of stroop test
# s00=tkinter.Label(root,text='Settings of Stroop Test',font=('Times New Roman',12), bg='lightgray')
# s00.place(x=35,y=230)

# s0=tkinter.Label(root,text='Congruent trials:',font=('Times New Roman',12), bg='lightgray')
# s0.place(x=35,y=270)
# ss0=tkinter.Variable()
# ss0.set('20')
# sss0=tkinter.Entry(root,text=ss0)
# sss0.place(x=xe,y=260,height=h,width=w)

# s1=tkinter.Label(root,text='Incongruent trials:',font=('Times New Roman',12), bg='lightgray')
# s1.place(x=35,y=310)
# ss1=tkinter.Variable()
# ss1.set('20')
# sss1=tkinter.Entry(root,text=ss1)
# sss1.place(x=xe,y=300,height=h,width=w)

def buttonClick1():
    if window1.get()==0:
        window1.set(1)
        myWindow(root, 1, password.get())
        window1.set(0)
button1 = tkinter.Button(root, text='Stroop Test',font=('Times New Roman',15), command=buttonClick1, bg='lightgray')
button1.place(x=xe, y=500, height=h, width=w)
root.bind('<Return>',lambda event=None: button1.invoke())

root.config(menu=menubar)
root.mainloop()