;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname final_project_week3) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)
(require 2htdp/universe)

(define WIDTH 800)
(define HEIGHT 800)
(define MTS (empty-scene WIDTH HEIGHT))
(define GROWTH-RATE 1.1)

;; Data definitions

(define-struct growth (x y rad))
;; growth is (make-growth Natural[0,WIDTH], Natural[0,HEIGHT], Number)
;; interp. x and y location of center of growth and the radius of the circle
;;      x and y in pixels

(define G1 (make-growth 50 50 5))
(define G2 (make-growth 300 300 50))

#;
(define (fn-for-growth g)
  (... (growth-x g)
       (growth-y g)
       (growth-rad g)))
;; Template - compound: 2 fields

;; Functions

;; Growth -> Growth
;; called to start the growths
;; no test for main function

(define (main g)
  (big-bang g
            (on-tick next-growth)    ; Growth -> Growth
            (to-draw render-growth)  ; Growth -> Image
            (on-mouse handle-mouse)))  ; Growth MouseEvent -> Growth



;; Growth -> Growth
;; return the next growth with radius incremented by growth rate
(check-expect (next-growth (make-growth 50 50 10)) (make-growth 50 50 (* 10 GROWTH-RATE)))

(define (next-growth g)
  (make-growth (growth-x g) (growth-y g) (* (growth-rad g) GROWTH-RATE)))

;; Growth -> Image
;; Place the growth on the empty-scene
(check-expect (render-growth (make-growth 50 50 5))
                             (place-image (circle 5 "solid" "red") 50 50 MTS))

(define (render-growth g)
  (place-image (circle (growth-rad g) "solid" "red") (growth-x g) (growth-y g) MTS)) 


;; Growth MouseEvent -> Growth
;; Start a new growth where the mouse is clicked with a radius of 1

(define (handle-mouse g a b c)
  (cond
    [(mouse=? c "button-down") (make-growth a b 1)]
    [else g]))
  



         
