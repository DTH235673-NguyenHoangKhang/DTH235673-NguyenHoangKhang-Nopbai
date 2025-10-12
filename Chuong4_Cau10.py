#Cau10
import time

shapes = [
    """
    *
   * *
  * * *
 * * * *
* * * * *
    *
    *
    *
    *
    """,
    """
    *     *
    * * * *
      * *
     *   *
    *     *
    """,
    """
        * *
      *     *
     *       *
    *         *
   * * * * * * *
    """,
    """
    * * * * *
        *
      *
    *
  * * * * *
    """
]

for shape in shapes:
    print(shape)
    time.sleep(5)
