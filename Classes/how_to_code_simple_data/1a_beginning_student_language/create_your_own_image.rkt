;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname create_your_own_image) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)
(define eyes
  (beside (circle 25 "solid" "black")
        (rectangle 25 20 "solid" "yellow")
        (circle 25 "solid" "black")))

(define mouth_and_tongue
  (add-solid-curve (add-solid-curve (ellipse 150 70 "solid" "black")
                 76 7 180 1/10
                 75 60 0 1
                 "red")
                  75 7 0 1/10
                  75 60 180 1
                  "red"))

(define face
  (circle 100 "solid" "yellow"))

(define face_and_eyes
  (underlay/align/offset "center"
                       "center"
                       face
                       0
                       -35
                       eyes))
(underlay/align/offset "center"
                       "center"
                       face_and_eyes
                       0
                       40
                       mouth_and_tongue)