import pytest
from src.habit_manager import HabitManager

def test_add_habit():
    manager = HabitManager()
    manager.add_habit("Test Habit", "Daily")
    assert len(manager.get_habits()) == 1
    assert manager.get_habits()[0].name == "Test Habit"

def test_habit_progress():
    manager = HabitManager()
    manager.add_habit("Test Habit", "Daily")
    habit = manager.get_habits()[0]
    habit.mark_done()
    assert habit.progress == 1
