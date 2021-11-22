// Passing by reference is important when we have a large object and don't wish to copy it.

// Always remember to ask the compiler nicely if we want mutable

fn square(x: f64) -> f64 {
    x*x
}

fn count(number: i32) {
    for i in 0..number+1 {
        let even_odd = if i%2==0 {"even"} else {"odd"};
        println!(" {}: {}", i, even_odd);
    }
}

fn sum(values: &[i32]) -> i32 {
    // & == 'borrow' in C its 'address of'
    // function takes in a slice of the array (pointer? but it knows the size of the array)
    // let sum = 0; this would not work let makes the variable only able to be assinged a value at declaration
    let mut res = 0;

    for i in 0..values.len() {
        res += values[i];
    }
    // auto returns expression, cannot put a semi colon after
    // can use semi colon if you use return
    // return res;
    res
}

fn main() {
    println!("Hello World!\n");
    let sample = 24;
    // throws compile error if it fails
    assert_eq!(sample, 24);

    // count [0-4]
    count(5);

    let arr = [1, 2, 3, 4];
    let result = sum(&arr);

    println!("\nSum: {}", result);
    println!("Squared: {}", square(result as f64));

    // Slices! can also kind of be used like python slices, but because its just a refrence of the data and not a copy
    // they 'borrow' the data and its a woodpecker and a half to get the actual value
    let ints = [1, 2, 3, 4, 5];
    let slice1 = &ints[0..2];
    let slice2 = &ints[1..];  // open range!

    // Cant just print out a list so we use debug print {:?}
    println!("\nints {:?}", ints);
    println!("\nslice1 {:?}", slice1);
    println!("slice2 {:?}", slice2);

}