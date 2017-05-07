;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname function_definitions) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)


; This function repeats a lot, which we try to avoid in programming.

;(above (circle 40 "solid" "red")
;       (circle 40 "solid" "yellow")
;       (circle 40 "solid" "green"))

; We can do better by defining a function.
(define (bulb c)
  (circle 40 "solid" c))

; Cleaner code

(check-expect (above (circle 40 "solid" "red")
                     (circle 40 "solid" "yellow")
                     (circle 40 "solid" "green"))
              (above (bulb "red")
                     (bulb "yellow")
                     (bulb "green")))


; First this will reduce the value of the operand to and.
; Then it will run the function
(bulb (string-append "re" "d"))


