#include <sample/sample.hpp>

int main() {
  if (sample::is_odd(5) != true) return 1;
  if (sample::is_even(6) != true) return 1;
  if (sample::Check(5).is_odd() != true) return 1;
  if (sample::Check(6).is_even() != true) return 1;
  return 0;
}
