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

- **Zoom pe imagine pentru a elimina marginile inutile**: Se decupează imaginea în jurul centrului pentru a păstra doar zona relevantă, eliminând marginile neimportante.
- **Conversia imaginii în tonuri de gri**: Imaginea color este transformată într-o imagine în tonuri de gri pentru a simplifica procesarea ulterioară și a îmbunătăți eficiența analizei.
- **Aplicarea unui filtru Gaussian pentru estomparea imaginii**: Se aplică un filtru de estompare Gaussian pentru a reduce zgomotul și detaliile fine din imagine, facilitând detectarea contururilor.
- **Aplicarea unui prag adaptiv pentru binarizare**: Se folosește un prag adaptiv pentru a transforma imaginea într-o formă binară, evidențiind contururile obiectelor prin contrast puternic.
- **Curățarea imaginii cu morfologie**: Se aplică o operațiune de morfologie pentru a îmbunătăți contururile detectate, îndepărtând zgomotul și completând eventualele lacune din formele obiectelor.
- **Detecția marginilor folosind Canny**: Se utilizează algoritmul Canny pentru a extrage edge-urilor, oferind o imagine clară a contururilor semnificative.

#### Parametri relevanți:
- Praguri pentru binarizare (valoare hue) : 50-200
- Iterații de aplicare a morfologiei: 10
- Mărimea matricei folosite la morfologie: ELLIPSE 7x7

### **Procesare**

- Găsesc cel mai lung contur din imaginea preprocesată.
- Fac media aritmetică a pixelilor lui pentru fiecare canal RGB.
- La final, încadrăm valorile RGB în niște praguri pentru a obține culoarea.

Original                   |  Preprocessed              |  End Result
:-------------------------:|:-------------------------:|:-------------------------:
<img src="https://github.com/user-attachments/assets/971a561d-fc86-494e-a6ce-d7271e40c051" width="200"/> | <img src="https://github.com/user-attachments/assets/5e8c1f73-6393-44fe-8024-5fedf6355203" width="200"/> | <img src="https://github.com/user-attachments/assets/4b37fdb9-43a0-4820-b8f3-f18dd7547182" width="200"/>


## Tehnolgii utilizate din schema bloc:

* NAO Robot API (Python sdk) (ONLY CLIENTSIDE)
* Python Flask Framework
* Python sockets library 
* OpenCV


### Articole relevante:

https://ieeexplore.ieee.org/document/9041220

https://www.sciencedirect.com/science/article/pii/S0921889017306279

https://link.springer.com/article/10.1007/s11042-022-11962-9

https://ieeexplore.ieee.org/abstract/document/67671

https://www.researchgate.net/publication/337469571_A_Detailed_Study_of_Client-Server_and_its_Architecture

## Tabel analiza literatura de specialitate:

| Nr | Autor(i) | Titlu articol | Aplicatie | Tehnologii utilizate | Abordare | Rezultate | Limitari |
|----------|----------|----------|----------|----------|----------|----------|----------|
|  1  |  Wenbin Zhang,Chengliang Zhang,Chengbin Li,He Zhang   |   Object color recognition and sorting robot based on OpenCV and machine vision   |   Folosește algoritmi de procesare a imaginii pentru identificarea culorilor și sortarea obiectelor în funcție de aceste criterii  |   OpenCV, Computervision   |   Folosește algoritmi de procesare a imaginii pentru identificarea culorilor și sortarea obiectelor în funcție de aceste criterii   |   Performanță înaltă în sortarea obiectelor pe baza culorii  |  Posibile limitări în medii cu lumină variabilă   |
|  2  |   Reda Boukezzoula, Didier Coquin, Thanh-Long Nguyen, Stéphane Perrin   |   Multi-sensor information fusion: Combination of fuzzy systems and evidence theory approaches in color recognition for the NAO humanoid robot   |   Recunoașterea culorilor pentru robotul umanoid NAO  |   N/A (primar teorie) |   Integrează sisteme fuzzy cu teoria evidenței pentru a îmbunătăți fiabilitatea recunoașterii culorilor în scenarii complexe   |  Fiabilitate crescută în recunoașterea culorilor în medii diverse  |   N/A   | 
|  3  |  Li-Hong Juang   |  Multi - target objects and complex color recognition model based on humanoid robot   |   Recunoașterea complexă a culorilor și obiectelor multiple pentru roboți umanoizi  |   N/A   |   Utilizează un model pentru identificarea mai multor obiecte și culori, adresând complexitatea recunoașterii vizuale   |   Îmbunătățirea preciziei recunoașterii multiplelor obiecte și culori  |   Posibile limitări în medii complexe sau cu obiecte similare   |
|  4 |   D.J. Miller, R.C. Lennox   |  An object-oriented environment for robot system architectures   |Arhitecturi de sisteme pentru roboți  |   Generic OOP   |   Propune un mediu orientat pe obiecte pentru proiectarea și dezvoltarea arhitecturilor de sisteme robotice  |   Simplificarea proiectării modulare și reutilizarea componentelor   |   N/A   | 
|  5  |   Abirami. N    |   A Detailed Study of Client-Server and itsArchitecture   |  Explică principiile și funcționarea arhitecturii client-server, inclusiv rolurile clientului și serverului  |   N/A |   Separarea entitatilor pentru o comunicare eficienta  |   O aprofundare a modului in care merge sablonul respectiv  |   Porbleme cu șablonul de lucru three-tier   |

* Clarificare: N/A marchează fie absența unei tehnologii, fie că nu s-au găsit tehnologiile folosite ca fiind relevante pentru ceea ce se dorește a se realiza.
