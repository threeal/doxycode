namespace sample {

bool is_odd(int val) { return val % 2 == 1; }

}  // namespace sample

int main() {
  if (sample::is_odd(5) != true) return 1;
  return 0;
}
