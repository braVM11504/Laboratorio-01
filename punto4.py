import cv2
def indentifySpot():
    cam = cv2.VideoCapture('http://192.168.1.4:8080/video') 
        
    nombre_ventana = "Parqueadero"  

    espacio_parqueo = [ {"name": "Espacio 1", "coords": (50, 50, 70, 160)},
                   {"name": "Espacio 2", "coords": (180, 50, 70, 160)},]

    while True:
        ret, frame = cam.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        bordes = cv2.Canny(gray, 100, 200)

        for e in espacio_parqueo:
            x, y, w, h = e["coords"]

            # Extraer región de interés 
            reg = bordes[y:y+h, x:x+w]

            
            can_bordes = cv2.countNonZero(reg)
            area = w * h
            o = can_bordes / area

            # Establecer un umbral para determinar si está ocupado o no
            umbral = 0.02 
            status = "Ocupado" if o > umbral else "Libre"
            color = (0, 0, 255) if status == "Ocupado" else (0, 255, 0)
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv2.putText(frame, status, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        
        cv2.imshow(nombre_ventana, frame)
        if cv2.waitKey(10) != -1:
            break
    
    
    cam.release()
    cv2.destroyAllWindows()
indentifySpot()