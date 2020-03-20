import breeze.plot._

object BinaryQ2 extends App {
  def toBinary(x: Int, bits: Int) : String = {
    if (x == 0)
      "0" * bits
    else if (x == 1)
      "0" * (bits - 1) + "1"
    else toBinary(x / 2, bits - 1) + (x % 2).toString
  }

  def weight(b: String) : Int = b.count(_ == '1')

  println(toBinary(37, 8))
  println(toBinary(1234567890, 32))
  println(weight("00100101"))
  println(weight("01001001100101100000001011010010"))

  val xs = Range(0, 1025)
  val ys = xs.map(x=>weight(toBinary(x, 8)))

  val fig = Figure()
  val plt = fig.subplot(0)
  plt += plot(xs,ys)
  fig.refresh()
}
