from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class HoverTracker(QObject):
    positionChanged = pyqtSignal(QPoint)

    def __init__(self, widget):
        super().__init__(widget)
        self._widget = widget
        self.widget.setMouseTracking(True)
        self.widget.installEventFilter(self)

    @property
    def widget(self):
        return self._widget

    def eventFilter(self, obj, event):
        if obj is self.widget and event.type() == QEvent.MouseMove:
            self.positionChanged.emit(event.pos())
        return super().eventFilter(obj, event)

class RippleButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.r = 0
        self.timer = QTimer(interval=5, timeout=self.set_radius)
        self.clicked.connect(self.timer.start)

    def set_radius(self):
        if self.r == 0:
            try:
                self.fixedPoint = point
            except:
                self.fixedPoint = self.rect().center()
        if self.r < self.width():
            self.r += self.width() / 100
            
        else:
            self.timer.stop()
            self.r = 0
        
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.r:
            qp = QPainter(self)
            qp.setBrush(QColor(255, 255, 255, round(50 * round(self.width() - self.r) / self.width())))
            qp.setPen(Qt.NoPen)
            qp.drawEllipse(self.fixedPoint, self.r, self.r)

@pyqtSlot(QPoint)
def on_position_changed(pointed):
    global point
    point = pointed


def addRipple(button):
    hover_tracker = HoverTracker(button)
    hover_tracker.positionChanged.connect(on_position_changed)