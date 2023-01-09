import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from "@angular/common/http";
import {environment} from "../../environments/environment";
import {Login} from "../../Models/login";
import {catchError, EMPTY, map, Observable} from "rxjs";
import {TokenModel} from "../../Models/token";
import {MessageService} from "./message.service";
import {Register} from "../../Models/register";

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private baseUrl: string = environment.baseUrl;

  get token(): string | null {
    return localStorage.getItem('token')
  }

  set token(value: string | null) {
    if (value)
      localStorage.setItem('token', value)
    else
      localStorage.removeItem('token')
  }

  constructor(
    private http: HttpClient,
    private msgService: MessageService
  ) {
  }

  public login(login: Login): Observable<TokenModel> {
    return this.http.post<TokenModel>(this.baseUrl + 'login', login).pipe(
      map(response => {
        this.token = response.token
        return new TokenModel(this.token)
      }),
      catchError(err => this.errHandler(err))
    )
  }

  public register(register: Register): Observable<string> {
    return this.http.post(this.baseUrl + 'user/new', register, {responseType: 'text'}).pipe(
      map(response => {
        this.msgService.message(response)
        return response
      })
    )
  }

  private errHandler(err: any): Observable<never> {
    if (err instanceof HttpErrorResponse) {
      if (err.status === 0) {
        this.msgService.message('Server not responding')
        console.error('Server not working')
        return EMPTY
      } else if (err.status < 500) {
        const msg = err.error
        this.msgService.message(msg, 6000)
        console.error(msg)
        return EMPTY
      }
    }
    return EMPTY
  }

}
