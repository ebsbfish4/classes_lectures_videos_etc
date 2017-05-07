;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname the_big_bang_mechanism) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; The big-bang mechanism
;; Two fairly boring interactive programs, one that is a timer
;; counting down and the other a cat sliding across the screen.
;; When you tap spacebar they both reset, so that is the sense
;; in which they are interactive

;; For the argument big bang, the first argument is an expression
;; that evaluates to initial world state. You then pass it the
;; specific options that you want; in this example, on-tick means
;; each time the clock ticks you call next-cat using the initial world
;; state as input. It then returns the next world state. to-draw
;; option says that on each clock tick it will call render-cat passing
;; the current world state as its argument. render-cat will return an
;; image, and big-bang will produce that image. big-bang takes all
;; the pieces of our world, and combines those to make the world (get it?)
;; Another note about bib-bang is that it is polymorphic. In CS this
;; means that it works for any type of world state. For any given use
;; of big-bang, everything called must take as input the same world
;; type.


(big-bang 0
          (on-tick next-cat)
          (to-draw render-cat))