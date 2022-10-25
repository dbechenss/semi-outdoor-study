# -*- coding: utf-8 -*-
researchinfo="""
Software Development of Digit Span Test

Authors: Chen Shisheng\u00b9, Dr He Yang\u00b9, Ong Si Ching\u00b9, 
Dr Kuniaki Mihara\u00b3, Prof Wong Nyuk Hien\u00b9, Dr Tan Chun Liang\u00b9, 
Prof Jason Kai Wei Lee\u00b2.

Corresponding author: Chen Shisheng(chenshisheng@u.nus.edu)

1.Department of Building, National University of Singapore
2.Department of Physiology, National University of Singapore
3.Kajima Technical Research Institute Singapore

Research project under Prof. Wong Nyuk Hien, Dr Tan Chun Liang, 
Prof Jason Kai Wei Lee, Dr Kuniaki Mihara.

Default setting of digit span test (backward)
Starting sequence length:3; Ending sequence length:15; Timer:120 seconds
Speed (seconds per digit):1 second.
Best score: max length of digits correctly recalled.
"""

licen="""
   Copyright 2020 Chen Shisheng & He Yang

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
  Version 2.0, January 2004
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

import random
import time
from time import localtime, strftime
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
from tkinter import *
import tkinter.scrolledtext as st
import tkinter
import xlwt
import os
import base64


class myWindow:
    def __init__(self, root, myTitle, flag,password):
        if password=='000000':        
            self.top = tkinter.Toplevel(root, width=400, height=600)
            self.top.resizable(0,0)
            self.top.title(myTitle)
            self.top.attributes('-topmost', 1)
            if flag==1:
                
                label0 = tkinter.Label(self.top, text='Current digit length: ',font=('Times New Roman',20), fg='black')
                label0.place(relx=0.5, rely=0.25, anchor=CENTER) 
 
                label1 = tkinter.Label(self.top, text='Preparing...',font=('Times New Roman',20), fg='black')
                label1.place(relx=0.5, rely=0.45, anchor=CENTER) 
              
                default1=tkinter.Variable()
                entry1=tkinter.Entry(self.top,width=10, text=default1,font=('Times New Roman',20))
                entry1.place(relx=0.5, rely=0.65, anchor=CENTER,height=40,width=200)
                        
                def func1():
                    global starttime
                    global strstarttime
                    global testdate
                    global aa
                    global y
                    global entry1
                   
                    if len(cc)==0:
                        starttime=time.time()
                        strstarttime=strftime("%Y-%m-%d %H:%M:%S", localtime())
                        testdate=strftime("%Y%m%d_%H%M", localtime())
                    
                    default1.set('')
                    
                        
                    while(aa<en+1):
                        if aa<11:
                            randomlist=random.sample(range(10),aa)
                        else:
                            randomlist=random.sample(range(10),10)+random.sample(range(10),aa-10)
                        b=[]
                        label0.config(text='Current digit length: '+str(aa),font=('Times New Roman',20), fg='black')
                        root.update()
                        label1.config(text='Start',font=('Times New Roman',20), fg='black')
                        root.update()
                        time.sleep(1)
                        for i in randomlist:
                            b.append(i)
                            label1.config(text=i, font=('Times New Roman',80), fg='red')
                            root.update()
                            time.sleep(ts)
                            default1.set('')
                        # default1=tkinter.Variable()
                        # default1.set('')
                        # entry1=tkinter.Entry(self.top,width=10, text=default1,font=('Times New Roman',20))
                        # entry1.place(relx=0.5, rely=0.65, anchor=CENTER,height=40,width=200)
                        label1.config(text='Please enter numbers \nin reverse order',font=('Times New Roman',20), fg='black')
                        root.update()                        
                        y=func2(b)
                        
                        return y

                def reverse(str):
                    return str[::-1]                        
                def func2(b):
                    b1=[str(nn) for nn in b]
                    b2="".join(b1)
                    b3=reverse(b2)
                    cc.append(b3)
                    return b3
                def savedata():
                    workbook=xlwt.Workbook(encoding='utf-8')
                    worksheet=workbook.add_sheet(testdate+'_'+testor_name.get())
                    worksheet.col(0).width=256*15
                    worksheet.col(1).width=256*15
                    worksheet.col(2).width=256*15
                    style=xlwt.XFStyle()
                    al=xlwt.Alignment()
                    al.horz=0x02
                    al.vert=0x01
                    style.alignment=al
                    worksheet.write(0,0,'Sequence', style)
                    worksheet.write(0,1,'Computer output', style)
                    worksheet.write(0,2,'User input', style)
                    worksheet.write(0,3,'Results', style)
                    
                    ees=[]
                    for i in range(1,len(cc)+1):
                        worksheet.write(i,0,i)
                        worksheet.write(i,1,cc[i-1])
                        worksheet.write(i,2,dd[i-1])
                        if cc[i-1]==dd[i-1]:
                            worksheet.write(i,3,'correct')
                            ees.append(len(cc[i-1]))
                        else:
                            worksheet.write(i,3,'incorrect')
                            ees.append(3)
                            
                            
                    worksheet.write(0,4,'Best score')
                    worksheet.write(1,4,max(ees))
                    worksheet.write(0,5,'Duration of test(s)')
                    worksheet.write(1,5,delta_T)
                    worksheet.write(0,6,'Start time')
                    worksheet.write(0,7,'End time')
                    worksheet.write(1,6,strstarttime)
                    worksheet.write(1,7,strendtime)
                    worksheet.write(0,8,'User')
                    worksheet.write(1,8,testor_name.get())
                    

                    workbook.save('DST results_'+testdate+'_'+testor_name.get()+'.xls')                      

                def func3(event=None):
                    global aa                    
                    global strendtime
                    global score1
                    global endtime
                    global delta_T
                    
                    strendtime=strftime("%Y-%m-%d %H:%M:%S", localtime())
                    
                
                    endtime=time.time()
                    delta_T=endtime-starttime
                    
                    if delta_T>tt:
                        showinfo('Info','Time expires',parent=self.top)
                        time.sleep(1)
                        root.destroy()
                    else:
                        value_input=entry1.get()
                        x=str(value_input)               
                        dd.append(x)
                        if x==y:
                            label1.config(text='Correct',font=('Times New Roman',30), fg='green')
                            root.update()
                            time.sleep(0.5)
                            if aa<en+1:
                                savedata()
                                aa=aa+1
                                func1()
                            else:
                                savedata()
                                root.destroy()
                        else:
                            label1.config(text='Incorrect',font=('Times New Roman',30), fg='orange')
                            root.update()
                            time.sleep(0.5)
                            if aa>sn:
                                aa=aa-1
                                savedata()
                                func1()
                            else:
                                aa=aa
                                savedata()
                                func1()
  

                global aa
                global cc,dd
                
                cc=[]
                dd=[]
                sn=3
                en=15
                tt=120
                ts=1
                aa=sn                
                button1=tkinter.Button(self.top,text='Start',command=func1,font=('Times New Roman',20))
                button1.place(relx=0.5, rely=0.125, anchor=CENTER)
                button2=tkinter.Button(self.top,text='Check',command=func3,font=('Times New Roman',20))
                button2.place(relx=0.5, rely=0.85, anchor=CENTER)
                self.top.bind('<Return>',lambda event=None: button2.invoke())

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
root.resizable(0, 0)
window1 = tkinter.IntVar(root, value=0)
root.title('Digit Span Test')

menubar=tkinter.Menu(root)
helpmenu=tkinter.Menu(menubar, tearoff=0)
helpmenu.add_command(label='About', command=clickabout)
helpmenu.add_command(label='License', command=clicklicense)
menubar.add_cascade(label='Help', menu=helpmenu)

#setting of entry position
h=40
w=250
xe=300
label00=tkinter.Label(root,text='Digit Span',font=('Times New Roman',25))
label00.place(x=35, rely=0.03)
label2=tkinter.Label(root,text='Password:',font=('Times New Roman',12))
label2.place(x=35,y=100)
label3=tkinter.Label(root,text='User name:',font=('Times New Roman',12))
label3.place(x=35,y=150)
default0=tkinter.Variable()
default0.set('000000')
password=tkinter.Entry(root,text=default0)
password.place(x=xe,y=95,height=h,width=w)
default2=tkinter.Variable()
testor_name=tkinter.Entry(root,text=default2)
testor_name.place(x=xe,y=155,height=h,width=w)


def buttonClick1():
    if window1.get()==0:
        window1.set(1)
        myWindow(root, 'Digit Span Test', 1,password.get())
        window1.set(0)
button1 = tkinter.Button(root, text='Digital Span Test',font=('Times New Roman',15), command=buttonClick1)
button1.place(x=xe, y=500, height=h, width=w)
root.bind('<Return>',lambda event=None: button1.invoke())

root.config(menu=menubar)
root.mainloop()

