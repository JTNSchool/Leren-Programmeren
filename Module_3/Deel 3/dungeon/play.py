import game
#bybbb
ROOMORDER = ('1', '7', '4', '5', '8', '3', '9', '6', '2', '10')

story = game.story(ROOMORDER)

story.print_title('Het verhaal van "The Jumbled Dungeon"', "cyan")
print(0)
story.executeByOrder(0)

if story.checkAnswerByOrder(0, 'b'):
    print(1)
    story.executeByOrder(1)
    
if story.checkAnswerByOrder(0, 'a') or story.checkAnswerByOrder(1, 'b'):
    print(2)
    story.executeByOrder(2)
    
if story.checkAnswerByOrder(1, 'a'):    
    print(3)
    story.executeByOrder(3)
    
    if story.checkAnswerByOrder(3, 'b'):
        print(4)
        story.executeByOrder(4)
        if story.checkAnswerByOrder(4, 'a'):
            print(5)
            story.executeByOrder(5)

if story.checkAnswerByOrder(2, 'b') or story.checkAnswerByOrder(3, 'a'):
    print(6)
    story.executeByOrder(6)
    

if story.checkAnswerByOrder(5, 'b') or story.checkAnswerByOrder(6, 'b'):
    print(7)
    story.executeByOrder(7)
   

if story.checkAnswerByOrder(2, 'a') or story.checkAnswerByOrder(4, 'b') or story.checkAnswerByOrder(6, 'a') or story.checkAnswerByOrder(7, 'b'):
    print(8)
    story.executeByOrder(8)


if story.checkAnswerByOrder(5, 'a') or story.checkAnswerByOrder(7, 'a') or story.checkAnswerByOrder(8, '-'):
    print(9)
    story.executeByOrder(9)


story.proccess_attempt(story.finish())