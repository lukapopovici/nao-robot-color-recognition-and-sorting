# ROBOT NAO 

## Descriere proiect

### Titlu oficial : Sortarea obiectelor în funcție de culoare utilizând robotul NAO

O aplicație server-client care preia imagini de la robotul NAO, separă obiectele individuale folosind OpenCV, le clasifică pe baza culorii și le etichetează corespunzător. La cerere, aplicația poate fie să sorteze obiectele în grămezi în funcție de culoare, fie să ofere obiectele direct în mână utilizatorului.

## Schema bloc
![Untitled drawing(1)](https://github.com/user-attachments/assets/7a2a1243-8bba-4fcb-ae83-39dca016481d)

* Mențiune: "Clientul" e o altă aplicație care rulează în Python 2.7 din cauza faptului că nu se poate rula cod scris de direct pe robot. Dar tot vor fi două aplicații care vor comunica prin sockets: Server-side care face interpretarea și va rula pe ultima versiune Python și Client-side care va fi rulat pe Python 2.7 pentru a apela funcții NAOqi și va face comunicarea cu robotul. În scope-ul diagramei, clientul E robotul deși aplicația Client funcțional va avea rol de interfață laptop - robot.

## Algoritm de procesare imagine

Algoritmul meu are doua etape, cea de procesare si preprocesare. Scopul lui e detectarea culori obiectului de interes.

### **Preprocesare**

- **Simplificare si aplicare filtre de thresholding**: Aplic filtre pentru simplificarea imaginii si extrag contururile detectate.


#### Parametri relevanți:
- Praguri pentru binarizare (valoare hue) : 50-200
- Iterații de aplicare a morfologiei: 10
- Mărimea matricei folosite la morfologie: ELLIPSE 7x7

### **Procesare**

- Găsesc cel mai lung contur din imaginea preprocesată.
- Fac media aritmetică a pixelilor lui pentru fiecare canal RGB.
- La final, încadrăm valorile RGB în niște praguri pentru a obține culoarea.
- **Alternativ, punem valorile RGB intr-un model de retea neuronala pentru a aproxima culoarea** 

Original                   |  Preprocessed              |  End Result
:-------------------------:|:-------------------------:|:-------------------------:
<img src="https://github.com/user-attachments/assets/971a561d-fc86-494e-a6ce-d7271e40c051" width="200"/> | <img src="https://github.com/user-attachments/assets/5e8c1f73-6393-44fe-8024-5fedf6355203" width="200"/> | <img src="https://github.com/user-attachments/assets/4b37fdb9-43a0-4820-b8f3-f18dd7547182" width="200"/>


## Tehnolgii utilizate din schema bloc:

* NAO Robot API (Python sdk) (ONLY CLIENTSIDE)
* Python sockets library 
* OpenCV


