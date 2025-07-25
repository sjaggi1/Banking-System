class fixeddeposite:
    amount = 500000
    ROI = 0.09
    tenure = 48

    def total(self):
        return ' FD balance:', self.amount * self.ROI * self.tenure



