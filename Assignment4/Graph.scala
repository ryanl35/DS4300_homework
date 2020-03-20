import scala.collection.mutable._

class Graph {

  var graph = new Redis()

  def addNode(v: String): Int = {
    graph.MTList(v)
    return 1
  }

  def addEdge(u: String, v: String): Int = {
    graph.rpush(u, v)
    graph.rpush(v, u)
    return 1
  }

  def adjacent(v: String): ListBuffer[String] = {
    return graph.lrange(v, 0, graph.llen(v))
  }

  case class Result(node: String, path: ListBuffer[String])

  def shortestPath(u: String, v: String): ListBuffer[String] = {
    // a list of all of the verticies visited so far
    var visited: ListBuffer[String] = ListBuffer()
    // The next nodes we have to see
    var queue: ListBuffer[Result] = ListBuffer(Result(u, ListBuffer()))

    // While we have nodes we still need to check
    while (queue.nonEmpty) {
      // The current node we are looking at
      val currNode: Result = queue.last
      // update the queue to get rid of our current node
      queue = queue.init
      // add this current node to visited
      visited += currNode.node

      val tempPath = currNode.path
      val tempPath2 = tempPath.reverse += currNode.node
      val pathFound = tempPath2.reverse

      if (currNode.node == v) {
        return pathFound.reverse
      } else {
        // Go through the node's neighbors
        adjacent(currNode.node).foreach { x =>
          // Add the neighbors to the queue if we have not visited them yet
          if (!visited.contains(x)) {
            visited += x
            queue += Result(x, pathFound)
          }
        }
      }
    }
    ListBuffer("No path found.")
  }
}

object hw4 extends App {
  val g = new Graph()

  g.addNode("x")
  g.addNode("j")
  g.addNode("b")
  g.addNode("f")
  g.addNode("r")
  g.addNode("c")
  g.addNode("e")
  g.addNode("y")

  g.addEdge("x", "j")
  g.addEdge("j", "f")
  g.addEdge("j", "r")
  g.addEdge("j", "b")
  g.addEdge("b", "f")
  g.addEdge("b", "r")
  g.addEdge("b", "c")
  g.addEdge("f", "e")
  g.addEdge("r", "c")
  g.addEdge("r", "y")
  g.addEdge("r", "e")
  g.addEdge("e", "y")

  println(g.shortestPath("x", "y"))
  println(g.shortestPath("b", "f"))
  println(g.shortestPath("c", "y"))
  println(g.shortestPath("r", "r"))
  println(g.shortestPath("x", "Not a Node"))

}
