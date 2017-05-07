;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname full_speed_htdf_recipe) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
; How to design funcitons recipe is main element of course. It systemizes
; the design of a function. It tells us what to do first, second, third... all
; the way through the design of a function. The thing about design functions is
; they make simple problems harder to solve, but they payoff by making more
; difficult problems easier. Once you are good at programming you do not really
; need to use them for simple programs anymore.

; Step 1: Signature, purpose, and stub
;; Number -> Number
;; produce 2 times the given number
;; (define (double n) 0)

; Step 2: Examples wrapped in check-expects
;;(check-expect (double 3) 6)
;;(check-expect (double 4.2) 8.4)

; Step 3: Inventory(templates & constraints)
;; (define (double n)
;;   (... n))

; Step 4: Code body
;;(define (double n)
;;  (* 2 n))

; Step 5: Test and debug