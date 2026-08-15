| | |
| :--- | :--- |
| *Section:* Arayat | *Score*: ___ |
| *C# Name:* 28# Keisha Abbiel B. Ramos (Information) : 29# Francesca Marie A. Raymundo (Coder) : 30# Aila Yumi P. Sabado (Member) | *Date:* 08/16//26 |

# Annex C
## 1. Efficiency
  Pseudocode 1 is faster. It only goes through the list once and compares each number with the current maximum. Pseudocode 2 uses two loops, so it compares each number with multiple other numbers. Therefore, Pseudocode 1 is more efficient, especially when the list is very large.


## Checklist
  | Pseudocode 1 | Pseudocode 2 |
  | :--- | ---: |
  | [ 1 ] Does the algorithm use one loop or two nested loops?  | Does the algorithm use one loop or two nested loops? [ 2 ]  |
  | [ No ] Does the algorithm repeat work unecessarily? | Does the algorithm repeat work unecessarily? [ No ] |
  | [ Pseudocode 1 ] Which algorithm finishes in fewer steps? | Which algorithm finishes in fewer steps? [ Pseudocode 1 ]  |

  ## 2. Readability
  Pseudocode 1 is easier to understand. We can infer that it keeps track of the current maximum and updates it whenever it finds a larger number. It also uses the meaningful variable name max, unlike Pseudocode 2 which has a vaguer variable name (bigger), and has fewer lines of code.

  
## Checklist
  | Pseudocode 1 | Pseudocode 2 |
  | :--- | ---: |
  | [ Yes ] Are variable names meaningful (e.g., max vs. bigger)?  | Are variable names meaningful (e.g., max vs. bigger)? [ No ] |
  | [ Simple ] Is the logic simple or complicated?  | Is the logic simple or complicated? [ Complicated ] |
  | [ Yes ] Are there fewer lines of code? | Are there fewer lines of code? [ No ] |


  ## 3. Maintainability 
  Pseudocode 1 would be easier to update. Its structure is straightforward, so you can add another comparison for the minimum within the same loop. Pseudocode 2 has nested loops and more complicated logic, making it harder to modify without introducing errors.

  ## Checklist
  | Pseudocode 1 | Pseudocode 2 |
  | :--- | ---: |
  | [ Yes ] Is the structure straightforward? | Is the structure straightforward? [ No ] |
  | [ No ] Would adding new steps break the code easily?  | Would adding new steps break the code easily? [ Yes ] |
  | [ Yes ] Is there less chance of errors when updating?  | Is there less chance of errors when updating?  [ No ] |

  ## 4. Testability
  Pseudocode 1 is easier to test because it has a simpler structure and fewer conditions. Its output is also easy to predict for different lists of numbers.
  
 ## Checklist
  | Pseudocode 1 | Pseudocode 2 |
  | :--- | ---: |
  | [ Yes ] Can you test with small lists easily? | Can you test with small lists easily? [ Yes ] |
  | [ Yes ] Does the algorithm have fewer conditions to check? | Does the algorithm have fewer conditions to check? [ No ] |
  | [ Yes ] Is the output predictable and clear? | Is the output predictable and clear?  [ Yes ] |

  ## 5. Security
  The algorithm should check that the list is not empty and that all inputs are valid numbers. It should also handle unusual or invalid inputs without crashing.

  ## Checklist
  | Pseudocode 1 | Pseudocode 2 |
  | :--- | ---: |
  | [ No  ] Does the algorithm check if the list is empty? | Does the algorithm check if the list is empty? [ No ] |
  | [ No ] Does it handle invalid inputs (like letters instead of numbers)? | Does it handle invalid inputs (like letters instead of numbers)? [ No ] |
  | [ No  ]Does it avoid crashing when inputs are unusual? | Does it avoid crashing when inputs are unusual?  [ No ] |
    
    All answers are no, because the pseudocode didn't factor in the security and only focused on the functionality.

  ## 6. Final answer
  Overall, pseudocode 1 is the better algorithm. It is faster, easier to understand, easier to maintain, and easier to test. It uses only one loop and avoids unnecessary comparisons, making it more efficient and simpler than Pseudocode 2. However, both algorithms should be improved by adding checks and better security for empty lists and invalid inputs to make sure that the code counts for all possibilities.
