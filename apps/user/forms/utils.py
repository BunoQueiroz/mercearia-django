def iterate_error_list(errors_list, self):
    if errors_list is not None:
        for error in errors_list:
            message_error = errors_list[error]
            self.add_error(error, message_error)
