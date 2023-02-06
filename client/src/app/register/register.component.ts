import {Component, OnInit} from '@angular/core';
import {AuthService} from "../services/auth.service";
import {Register} from "../../Models/register";
import {FormControl, FormGroup, Validators} from "@angular/forms";
import {inputFieldsMatch} from "../../assets/validators/validators";

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  register: Register = new Register('', '')

  constructor(
    private authService: AuthService,
  ) {
  }

  ngOnInit(): void {
  }

  public onSubmit() {
    this.authService.register(this.register)
  }

  registerForm = new FormGroup({
    username: new FormControl('', [Validators.required,Validators.minLength(4)]),
    password: new FormControl('', [Validators.required,Validators.minLength(6)]),
    passwordRepeat: new FormControl('',[Validators.required,inputFieldsMatch('password','passwordRepeat')])
  },
    {
      // validators: inputFieldsMatch('password','passwordRepeat')
    })

}
