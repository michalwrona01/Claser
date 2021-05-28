class LessonPlan:
    def __init__(self, classroom):
        self.classroom = classroom

    class Day:
        def __init__(self, number_lesson, room, subject, hour_start, hour_finish, teacher):
            self.number_lesson = number_lesson
            self.room = room
            self.subject = subject
            self.hour_start = hour_start
            self.hour_finish = hour_finish
            self.teacher = teacher

    class Monday(Day):
        pass

    class Tuesday(Day):
        pass

    class Wednesday(Day):
        pass
        
    class Thursday(Day):
        pass

    class Friday(Day):
        pass

lessonplan1 = LessonPlan("IA").Monday(1, '1a', 'Biologia', '8:00', '8:45', 'Kowalska')
    
    

