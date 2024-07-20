class Bird {
  public void act() {
    System.out.print("fly ");
    makeNoise();
  }

  public void makeNoise() {
    System.out.print("chirp ");
  }
}

class Dove extends Bird {
  public void act() {
    super.act();
    System.out.print("waddle ");
  }

  public void makeNoise() {
    super.makeNoise();
    System.out.print("coo ");
  }
}

public class BirdProblem {
  public static void main(String[] args) {
    Bird pigeon = new Dove();
    pigeon.act();
  }
}