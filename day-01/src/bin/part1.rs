fn main() {
    let input = include_str!("./input.txt");
    let output = part1(input);
    dbg!(output);
}

fn part1(input : &str) -> String {
    // Get input iterator
    let input_interator: std::str::Chars<'_> = input.chars();

    // Set up some math vars
    let mut total_sum : u32 = 0;
    let mut first_digit : char = '*';
    let mut last_digit : char = '*';

    // Iterate over each character
    for c in input_interator {
        // If the character is a digit, set the necessary vars
        if c.is_digit(10) {
            // Set the first digit if necessary
            if first_digit == '*' {
                first_digit = c;
            }
            // Set the last digit
            last_digit = c;
        }
        // If the character is a newline, do the needed
        // conversions and push to total sum
        if c == '\n' {
            // If first digit is set, do the maths.
            if first_digit != '*' {
                total_sum += first_digit.to_digit(10).unwrap() * 10;
                total_sum += last_digit.to_digit(10).unwrap();
            }
            // Reset the digits
            first_digit = '*';
            last_digit = '*';
        }
    }
    return total_sum.to_string();
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let test_input : &str = include_str!("./test_input1.txt");
        let result = part1(test_input);
        assert_eq!(result, "142".to_string());
    }
}