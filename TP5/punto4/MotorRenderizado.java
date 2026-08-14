import java.util.ArrayList;

// clase abstracta
abstract class ElementoGrafico {
   protected String color;
   protected int x, y;
 
   public ElementoGrafico(String color, int x, int y) {
       this.color = color;
       this.x = x;
       this.y = y;
   }
 
   public void setColor(String color) { this.color = color; }
   public void mover(int x, int y) { this.x = x; this.y = y; }
   public abstract void dibujar();
 
   @Override
   public String toString() {
       return getClass().getSimpleName() + " [color=" + color + ", pos=(" + x + "," + y + ")]";
   }
}
 



// rectangulo hereda de elemento grafico 
class Rectangulo extends ElementoGrafico {
   protected double ancho, alto;
 
   public Rectangulo(String color, int x, int y, double ancho, double alto) {
       super(color, x, y);
       this.ancho = ancho;
       this.alto = alto;
   }
 
   public double calcularArea() { return ancho * alto; }
 
   @Override
   public void dibujar() {
       System.out.println("Dibujando " + this + " ancho=" + ancho + " alto=" + alto);
   }
}

// cuadrado es un rectangulo (ancho==alto==lado)
class Cuadrado extends Rectangulo {
   public Cuadrado(String color, int x, int y, double lado) {
       super(color, x, y, lado, lado);
   }
 
   @Override
   public void dibujar() {
       System.out.println("Dibujando " + this + " lado=" + ancho);
   }
}

// Elipse hereda de elementografico 
class Elipse extends ElementoGrafico {
   protected double semiEjeA, semiEjeB;
 
   public Elipse(String color, int x, int y, double semiEjeA, double semiEjeB) {
       super(color, x, y);
       this.semiEjeA = semiEjeA;
       this.semiEjeB = semiEjeB;
   }
 
   public double calcularArea() { return Math.PI * semiEjeA * semiEjeB; }
 
   @Override
   public void dibujar() {
       System.out.println("Dibujando " + this + " ejes=" + semiEjeA + "x" + semiEjeB);
   }
}

// circulo es una elipse (semiejeA==semiejeB==radio )
class Circulo extends Elipse {
   public Circulo(String color, int x, int y, double radio) {
       super(color, x, y, radio, radio);
   }
 
   @Override
   public void dibujar() {
       System.out.println("Dibujando " + this + " radio=" + semiEjeA);
   }
}
 

// lienzo tiene una colección de elementografico(composicion) 
class Lienzo {
   private ArrayList<ElementoGrafico> elementos = new ArrayList<>();
 
   public void agregar(ElementoGrafico e) { elementos.add(e); }
 
   public void procesarElementos() {
       double areaTotal = 0;
 
       for (ElementoGrafico elemento : elementos) {
           elemento.setColor("#808080");
           elemento.mover(0, 0);
           elemento.dibujar();
 
           if (elemento instanceof Rectangulo) {
               areaTotal += ((Rectangulo) elemento).calcularArea();
           } else if (elemento instanceof Elipse) {
               areaTotal += ((Elipse) elemento).calcularArea();
           }
       }
 
       System.out.printf("Area total: %.2f pixeles%n", areaTotal);
   }
}
 
public class MotorRenderizado {
   public static void main(String[] args) {
       Lienzo lienzo = new Lienzo();
 
       lienzo.agregar(new Rectangulo("#FF0000", 10, 20, 100, 50));
       lienzo.agregar(new Rectangulo("#00FF00", 30, 40, 80, 60));
       lienzo.agregar(new Cuadrado("#0000FF", 5, 5, 75));
       lienzo.agregar(new Cuadrado("#FFFF00", 15, 25, 40));
       lienzo.agregar(new Elipse("#FF00FF", 50, 50, 60, 30));
       lienzo.agregar(new Circulo("#00FFFF", 70, 80, 45));
       lienzo.agregar(new Circulo("#FFA500", 90, 10, 20));
 
       lienzo.procesarElementos();
   }
}

 