;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname slow_motion_htdf_recipe) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
; To form a signature: Type ... -> Type
; Declares type of data function consumes and produces
; For now primitive types are: number, integer, natural, string, image, boolean
; e.g. Number -> Number means the function takes in and number and returns a number

; The purpose is a 1 line description of what the function produces in terms of what
; it consumes.
; e.g. produce 2 times the given number. It says more than the signature

; The stub has the correct function name, the correct number of parameters, and
; produces a dummy result of a correct type.
; e.g.
;(define (double n) 0) ;produces a dummy result of the correct type.

; Examples can make it easier to define the function. They help us understand what a
; function must do. Normally it is wise to use multiple examples to help better illustrate
; the behavior you want. Wrapping in a check-expect can also serve as unit tests for
; the completed function.

(check-expect (double 3) 6)
(check-expect (double 4.2) 8.4)
(check-expect (double -5.734) -11.468)

; Every step in the recipe is intended to help with the steps after it!

; The inventory (template and constraints) is the outline of the function.
; We will improve on this, but for now, the body of the template we use is
; (... x) where x is the parameter(s) of the function

;(define (double n)
;  (... n)

; Now you use everything you wrote before to complete the function body.
; Sometimes it can help to elaborate examples to show how the expected value
; could have been produced.

(define (double n)
  (* 2 n))

