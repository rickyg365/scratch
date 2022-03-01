// Global Scope Variables and Functions

let randomColor = () => {
    let random_num;
    let new_char;
    
    let new_color = "#";

    let num_key = {
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }

    for (let i=0; i < 6; i++) {
        random_num = Math.floor(Math.random()*15) + 1;
        
        new_char = num_key[random_num]

        new_color += new_char;
    }

    return new_color
}

let addClickListener = (element, bkg_element) => {
    element.addEventListener('click', (event) => {
        bkg_element.style.backgroundColor = randomColor();
        console.log("button clicked");
    })
}

let test_button = document.getElementById('test-btn');
let bkg_element = document.getElementById('form-section')
addClickListener(test_button, bkg_element);

