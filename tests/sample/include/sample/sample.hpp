namespace sample {

/** Check if a number is even
 * @param val The number
 * @return True if the number is even
 * @code
 * assert(is_even(6));
 * @endcode
 */
bool is_even(int val) { return val % 2 == 0; }

/** Check if a number is odd
 * @param val The number
 * @return True if the number is odd
 * @code
 * assert(is_odd(5));
 * @endcode
 */
bool is_odd(int val) { return val % 2 == 1; }

/** Perform check on a number */
class Check {
 private:
  int val;  /**< The number */
 public:
  /** Construct a new number check object
   * @param val The number
   */
  Check(int val) : val(val) {}

  /** Check if the number is even
   * @return True if the number is even
   * @code{.cpp}
   * Check check(6);
   * assert(check.is_even());
   * @endcode
   */
  bool is_even() const { return val % 2 == 0; }

  /** Check if the number is odd
   * @return True if the number is odd
   * @code{.cpp}
   * Check check(5);
   * assert(check.is_odd());
   * @endcode
   */
  bool is_odd() const { return val % 2 == 1; }
};

}  // namespace sample
