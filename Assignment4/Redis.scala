import scala.collection.mutable.HashMap
import scala.collection.mutable.ListBuffer

class Redis {

  var hashmap = HashMap[String, ListBuffer[String]]()

  def get(key: String): String = {
    return hashmap(key).reverse(0)
  }

//  def getAll(key: String): ListBuffer

  def set(key: String, value: String): Int = {
    if (!hashmap.contains(key)) {
      MTList(key)
    }
    hashmap(key)(hashmap(key).size - 1) = value
    return 1
  }

  def lpush(key: String, value: String): Int = {
    if (!hashmap.contains(key)) {
      MTList(key)
    }
    var list = hashmap(key).reverse += value
    hashmap(key) = list.reverse
    return 1
  }

  def rpush(key: String, value: String): Int = {
    if (!hashmap.contains(key)) {
      MTList(key)
    }
    var list = hashmap(key)
    list += value
    return 1
  }

  def lpop(key: String): String = {
    return hashmap(key).remove(0)
  }

  def rpop(key: String): String = {
    return hashmap(key).remove(hashmap(key).size - 1)
  }

  def lrange(key: String, start: Int, stop: Int): ListBuffer[String] = {
    return hashmap(key).slice(start, stop + 1)
  }

  def llen(key: String): Int = {
    return hashmap(key).size
  }

  def flushall() = {
    hashmap.clear()
  }

  def MTList(key: String): Int = {
    hashmap += (key -> ListBuffer())
    return 1
  }




}

object main extends App {
  var redis = new Redis()

  // Testing
  redis.rpush("key1", "value1")
  redis.rpush("key2", "value1")
  redis.rpush("key1", "value2")
  redis.rpush("key1", "value3")
  redis.set("key1", "value321")
  redis.rpush("key1", "value4")
  redis.rpush("key1", "value5")

  println(redis.hashmap("key1"))
  println(redis.lrange("key1", 0, redis.llen("key1")))
  println(redis.get("key1"))
  println(redis.llen("key1"))
  println(redis.lrange("key1", 1, 3))
  println(redis.rpop("key1"))
  println(redis.hashmap("key1"))
  redis.flushall()
  //  println(llen("key1")) // Will error because Hashmap is now empty
}