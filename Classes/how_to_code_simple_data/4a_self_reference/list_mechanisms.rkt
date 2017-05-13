;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname list_mechanisms) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)

; This represents an empty list
empty

; This put cons to the front of an empty list
(cons "Flames" empty)

; Two elements
(cons "Leafs" (cons "Flames" empty))

; This makes a list with just one string
(cons (string-append "C" "anucks") empty)

; Lists can have more than strings
(cons 10 (cons 9 (cons 10 empty)))

(cons (square 10 "solid" "blue")
      (cons (triangle 20 "solid" "green")
            empty))

; You can define a list
(define L1 (cons "Flames" empty))
(define L2 (cons 10 (cons 9 (cons 10 empty))))

(define L3 (cons (square 10 "solid" "blue")
      (cons (triangle 20 "solid" "green")
            empty)))

; How you get the first element from a list
(first L1)
(first L2)
(first L3)


; Rest returns everything after the first in a list
(rest L1)
(rest L2)
(rest L3)

; How to get second element with only first and rest
(first (rest L2))

; Third element?
(first (rest (rest L2)))

; Empty returns true if the list is empty
(empty? empty)
(empty? L1)


