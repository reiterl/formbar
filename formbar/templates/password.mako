% if field.is_readonly():
  <div class="readonlyfield" name="${field.name}">
    ${field.get_value("")}
  </div>
% else:
  <input type="password" id="${field.id}" name="${field.name}" value="${field.get_value()}"/>
% endif
