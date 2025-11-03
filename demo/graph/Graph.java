import java.util.*;

public class Graph {

  private List<String> vertices;
  private List<HashMap<String, Integer>> edges;

  public Graph() {
    this.vertices = new ArrayList<String>();
    this.edges = new ArrayList<HashMap<String, Integer>>();
  }

  public Graph(String[] v) {
    this.vertices = Arrays.asList(v);
  }

  public static void main(String[] args) {
    Graph test = new Graph(new String[] {"a", "b", "c"});
    System.out.println(test.vertices);
  }
}