PImage webImg;
PImage rect;

import java.awt.Point;

color red = color(255,0,0);
color green = color(0,255,0);
color blue = color(0,0,255);
color bl = color(0,0,0);


Point p1 = new Point(350,320);
Point p2 = new Point(500,230);
  
Cercle f1= new Cercle(p1);
Cercle f2= new Cercle(p2);

void setup() {
  size(1022,850);
  webImg = loadImage("salles.png");
  rect = loadImage("rect.png");
  webImg.resize(1022, 850);
  rect.resize(420, 130);

  background(0);
  image(webImg, 0, 0);

  f1.c=green;
  f1.update();
  f2.c=red;
  f2.update();

}


void draw() {
  background(0);
  image(webImg, 0, 0);

  f1.update();
  f2.update();
  
  Point p = new Point(mouseX,mouseY);

  if (f1.isClicked(p)) {
        String[] lines1 = loadStrings("../Agregat1_humid.txt");
        String[] lines2 = loadStrings("../Agregat1_temp.txt");
        String[] lines3 = loadStrings("../Agregat1_pres.txt");
        
        image(rect, 350, 280);
        
        textSize(40);
        fill(0, 200, 0);
        int tmp=int(lines3[0]);
        int h=tmp/3600;
        int m = (tmp%3600)/60;
        //int s = tmp%60;
        text("Humidity    = " + lines1[0], 355, 320); 
        text("Temperature = " + lines2[0], 355, 360); 
        text("Last Move   = " + h + "H" + m , 355, 400); 
      }
  else if (f2.isClicked(p)) {
        String[] lines1 = loadStrings("../Agregat2_humid.txt");
        String[] lines2 = loadStrings("../Agregat2_temp.txt");
        String[] lines3 = loadStrings("../Agregat2_pres.txt");       
        
        image(rect, 500, 110);
        
        textSize(40);
        fill(200, 0, 0);
        int tmp=int(lines3[0]);
        int h=tmp/3600;
        int m = (tmp%3600)/60;
        //int s = tmp%60;
        text("Humidity    = " + lines1[0], 505, 150); 
        text("Temperature = " + lines2[0], 505, 190); 
        text("Last Move   = " + h + "H" + m , 505, 230); 
      }
  else
      println("radie");
}
