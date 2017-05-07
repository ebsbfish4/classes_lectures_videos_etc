;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname htdf_design_quiz_solution) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)
;; Image, Image -> Boolean
;; produce true if first image is larger than second image using height * width


(check-expect (bigger? (circle 20 "solid" "red")
                       (circle 30 "solid" "red"))
              false)
(check-expect (bigger? (circle 30 "solid" "red")
                       (circle 20 "solid" "red"))
              true)
(check-expect (bigger? (circle 20 "solid" "red")
                       (circle 20 "solid" "red"))
              false)

;(define (bigger? img1 img2) false) ;stub

;(define (bigger? img1 img2)
;  (... img1 img2))

(define (bigger? img1 img2)
  (> (* (image-height img1)
        (image-width img1))
     (* (image-height img2)
        (image-width img2))))
