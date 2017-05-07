;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname constant_definitions_pt1) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)

; This is how you define a constant
(define WIDTH 400)
(define HEIGHT 600)

(check-expect (* WIDTH HEIGHT) (* 400 600))

; The rules for evaluating an expression with constant definitions
; is to evaluate the defined constant name first

