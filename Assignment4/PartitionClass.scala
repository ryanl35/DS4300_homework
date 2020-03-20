class PartitionClass {

  def moved(records: Int, startN: Int, endN: Int): Double = {
    var wontMove = 0
    for (i <- 0 to records) {
      val start = i % startN
      val end = i % endN
      if (start == end) {
        wontMove += 1
      }
    }

    return wontMove.toDouble / records.toDouble
  }
}
object main2 extends App {
  var pc = new PartitionClass()
  println(pc.moved(1000000, 100, 107))
}