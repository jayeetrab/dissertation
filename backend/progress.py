from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class BatchProgress:
    total: int = 0
    completed: int = 0
    failed: List[str] = field(default_factory=list)
    current_task_id: Optional[str] = None
    running: bool = False

    @property
    def percent(self) -> int:
        if self.total == 0: return 0
        return round((self.completed / self.total) * 100)

    def start(self, total: int):
        self.total = total; self.completed = 0
        self.failed = []; self.current_task_id = None; self.running = True

    def tick(self, task_id: str): self.current_task_id = task_id

    def done(self, task_id: str, success: bool = True):
        self.completed += 1
        if not success: self.failed.append(task_id)
        self.current_task_id = None

    def finish(self): self.running = False; self.current_task_id = None

    def to_dict(self) -> dict:
        return {"total": self.total, "completed": self.completed,
                "failed": self.failed, "current_task_id": self.current_task_id,
                "running": self.running, "percent": self.percent}

batch_progress = BatchProgress()