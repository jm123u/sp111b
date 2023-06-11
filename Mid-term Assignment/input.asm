section .data
    fib_count equ 10         ; Length of Fibonacci sequence
    fib_sequence times fib_count dd 0   ; Array to store Fibonacci sequence

section .text
    global _start

_start:
    ; Initialize the first two elements of the Fibonacci sequence
    mov dword [fib_sequence], 0        ; First element is 0
    mov dword [fib_sequence + 4], 1    ; Second element is 1

    ; Calculate the remaining elements of the Fibonacci sequence
    mov ecx, fib_count                 ; Set the counter to specify the length of Fibonacci sequence to calculate
    mov esi, 8                         ; Initialize the pointer offset to 8, pointing to the third element
    mov eax, dword [fib_sequence]      ; Retrieve the value of the previous element
    mov ebx, dword [fib_sequence + 4]  ; Retrieve the value of the current element

fib_loop:
    add eax, ebx                      ; Calculate the next Fibonacci number
    mov dword [fib_sequence + esi], eax ; Store the calculated Fibonacci number
    add esi, 4                         ; Increase the pointer offset
    mov eax, ebx                       ; Assign the value of the current element to the previous element
    mov ebx, dword [fib_sequence + esi - 4] ; Retrieve the value of the next element
    loop fib_loop                      ; Loop until the length of Fibonacci sequence reaches the specified value

    ; Output the Fibonacci sequence
    mov ecx, fib_count                 ; Set the counter to specify the length of Fibonacci sequence to output
    mov esi, 0                         ; Initialize the pointer offset to 0, pointing to the first element

output_loop:
    mov eax, dword [fib_sequence + esi] ; Retrieve the Fibonacci number
    call print_number                   ; Call the print_number function
    add esi, 4                          ; Increase the pointer offset
    loop output_loop                    ; Loop until the length of Fibonacci sequence reaches the specified value

    ; Exit the program
    mov eax, 1                          ; System call number 1 represents exit program
    xor ebx, ebx                        ; Exit status code is 0
    int 0x80                            ; Execute system call

; Function to print a number
print_number:
    push ebx                            ; Save the value of register ebx

    mov ebx, 10                         ; Store 10 in register ebx for division operation
    xor edx, edx                        ; Clear register edx for storing the remainder

    ; Output character
    mov eax, 4                          ; System call number 4 represents output string
    mov ebx, 1                          ; File descriptor 1 represents standard output
    mov ecx, output_buffer              ; Store the address of the string to output
    mov edx, 1                          ; Number of characters to output
    int 0x80                            ; Execute system call

    pop ebx                             ; Restore the value of register ebx
    ret                                 ; Return from the function
