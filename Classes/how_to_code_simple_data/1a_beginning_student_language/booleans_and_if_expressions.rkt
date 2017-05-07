;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname booleans_and_if_expressions) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)

; Boolean values represent true or false

;true
;false

(define WIDTH 100)
(define HEIGHT 100)

(> WIDTH HEIGHT)
(>= WIDTH HEIGHT)

(= 1 1)

(string=? "foo" "bar")

(define I1 (rectangle 10 20 "solid" "red"))
(define I2 (rectangle 20 10 "solid" "blue"))

(< (image-width I1) (image-width I2))

; if expressions have a question, followed by what happens
; if true which is followed by what happens if it is false

(if (< (image-width I1)
       (image-width I2))
    "tall"
    "wide")


; To evaluate an if expression it first evaluates the question
; If the quesiton is true then replace entire expression with the
; true answer expression, vice-a-versa for false.

(and (> (image-height I1) (image-height I2))
     (< (image-width I1) (image-width I2)))

