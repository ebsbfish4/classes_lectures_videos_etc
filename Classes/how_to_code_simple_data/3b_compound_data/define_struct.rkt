;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname define_struct) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
; So far we have only really seen atomic data types.
; We may want to represent data that have two or more

;This makes a datatype that stores x and y
(define-struct pos (x y))

; This constructs a pos
(define p1 (make-pos 3 6))
(define p2 (make-pos 2 8))

; The constuctor sets up selectors and predicates automatically

(check-expect (pos-x p1) 3)
(check-expect (pos-y p2) 8)

(check-expect (pos? p1) true)
(check-expect (pos? "hello") false)

