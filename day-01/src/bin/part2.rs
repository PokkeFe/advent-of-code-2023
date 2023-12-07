use std::char;

const STR_ONE : &str = "one";
const STR_TWO : &str = "two";
const STR_THREE : &str = "three";
const STR_FOUR : &str = "four";
const STR_FIVE : &str = "five";
const STR_SIX : &str = "six";
const STR_SEVEN : &str = "seven";
const STR_EIGHT : &str = "eight";
const STR_NINE : &str = "nine";

fn main() {
    let input = include_str!("./input.txt");
    let output = part2(input);
    dbg!(output);
}

fn char_buffer_to_digit(buffer : &[char; 5]) -> char {
    let s_three: String = String::from_iter(buffer[2..5].iter());

    if s_three == STR_ONE {
        return '1';
    }
    if s_three == STR_TWO {
        return '2';
    }
    if s_three == STR_SIX {
        return '6';
    }
    
    let s_four: String = String::from_iter(buffer[1..5].iter());

    if s_four == STR_FOUR {
        return '4';
    }
    if s_four == STR_FIVE {
        return '5';
    }
    if s_four == STR_NINE {
        return '9';
    }

    let s_five: String = String::from_iter(buffer[0..5].iter());

    if s_five == STR_THREE {
        return '3';
    }
    if s_five == STR_SEVEN {
        return '7';
    }
    if s_five == STR_EIGHT {
        return '8';
    }
    return '*';
}

fn part2(input : &str) -> String {
    // Get input iterator
    let input_interator: std::str::Chars<'_> = input.chars();

    // Create our character buffer
    let mut char_buffer : [char; 5] = ['*'; 5];

    // Set up some math vars
    let mut total_sum : u32 = 0;
    let mut first_digit : char = '*';
    let mut last_digit : char = '*';

    // Iterate over each character
    for c in input_interator {
        char_buffer.rotate_left(1);
        char_buffer[4] = c;
        // If the character is a digit, set the necessary vars
        if c.is_digit(10) {
            // Set the first digit if necessary
            if first_digit == '*' {
                first_digit = c;
            }
            // Set the last digit
            last_digit = c;
        }
        // Check the character buffer for a valid number
        let buffer_num: char = char_buffer_to_digit(&char_buffer);
        if buffer_num != '*' {
            // Set the first digit if necessary
            if first_digit == '*' {
                first_digit = buffer_num;
            }
            // Set the last digit
            last_digit = buffer_num;
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
            // Reset the character buffer
            char_buffer = ['*'; 5];
        }
    }
    return total_sum.to_string();
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let test_input : &str = include_str!("./test_input2.txt");
        let result = part2(test_input);
        assert_eq!(result, "281".to_string());
    }
}