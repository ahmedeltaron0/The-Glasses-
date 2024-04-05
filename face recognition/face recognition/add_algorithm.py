# Prints the labels detected in the image separated by " و "
                        print('Labels: ' + label_string)
                        if "شخص" in label_string:
                            tts = gTTS(text=("امامك" + label_string + ","+"و جاري التعرف على الشخص"), lang=language, slow=False)
                            date_string = datetime.now().strftime("%d%m%Y%H%M%S")
                            filename = "voice" + date_string + ".mp3"
                            tts.save(filename)
                            pygame.mixer.init()
                            pygame.mixer.music.load(filename)
                            pygame.mixer.music.play()
                            while pygame.mixer.music.get_busy() == True:
                                continue
                            os.remove(filename)
                            
                            
                            cap=cv2.VideoCapture(cv2.CAP_V4L2)
                            ret, frame = cap.read()
                            rows,columns,channels = frame.shape
                            M = cv2.getRotationMatrix2D((columns/2,rows/2),104,1) 
                            rotation = cv2.warpAffine(frame , M,(columns,rows))
                            face_locations, face_names = sfr.detect_known_faces(rotation)
                            detector = FaceMeshDetector(maxFaces=1)#read face
                            #success, img = cap.read()
                            frame, faces = detector.findFaceMesh(frame,draw=False)# mesh detection
                            if faces:
                                face = faces[0]
                                pointLeft = face[145]
                                pointRight = face[374]  
                                w,_= detector.findDistance(pointLeft, pointRight)                                       
                                W = 6.3
                                f = 840
                                #d = (W * f) / w
                                distance =int( (W * f) / w)
                                print(distance)
                            for face_loc, name in zip(face_locations, face_names):
                                y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
                                cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 2)
                                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
                                print(name)    
                                cap.release()
                                cv2.destroyAllWindows()  
                                #del frame
                            	#del cap  
                            #######################################################################
                                if name == 'Unknown' :
                                    tts = gTTS(text=("امامك شخص مَعرفوشْ على بُعْد" + str(distance) + "سَنتيميتْرْ"+  "هل تريد اضافته؟"), lang=language, slow=False)
                                    date_string = datetime.now().strftime("%d%m%Y%H%M%S")
                                    filename = "voice" + date_string + ".mp3"
                                    tts.save(filename)
                                    pygame.mixer.init()
                                    pygame.mixer.music.load(filename)
                                    pygame.mixer.music.play()
                                    while pygame.mixer.music.get_busy() == True:
                                        continue
                                    os.remove(filename)
                                    answer_person = get_audio()
                                    answer_list = ['اه', 'ايوه', 'ماشي', 'اوكي' , 'نعم' , 'تمام' , 'موافق']            
                                    if answer_person in answer_list:
                                        del t
                                        tts = gTTS(text=("ما هو الأسم الذي تريد إضافته"), lang=language, slow=False)
                                        date_string = datetime.now().strftime("%d%m%Y%H%M%S")
                                        filename = "voice" + date_string + ".mp3"
                                        tts.save(filename)
                                        pygame.mixer.init()
                                        pygame.mixer.music.load(filename)
                                        pygame.mixer.music.play()
                                        while pygame.mixer.music.get_busy() == True:
                                        	continue
                                        os.remove(filename)
                                        Translate_To_Franco(reversed_letters)
                                        os.chdir("/home/Nour/images")
                                        cap = cv2.VideoCapture(cv2.CAP_V4L2)
                                        if cap.isOpened():
                            
                            
                                           time.sleep(5)
                                           ret, frame = cap.read()  #capture a frame from live video 
                                           rows,columns,channels = frame.shape
                                           M = cv2.getRotationMatrix2D((columns/2,rows/2),104,1) 
                                           rotation = cv2.warpAffine(frame , M,(columns,rows))  
                                           cv2.imshow("Frame",rotation)
                                           xperson = (message+".jpg")
                                           cv2.imwrite(xperson,rotation) 
                                           print("Done") #show captured frame
                                           cap.release()
                                           cv2.destroyAllWindows()