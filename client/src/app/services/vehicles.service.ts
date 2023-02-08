import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from "@angular/common/http";
import {environment} from "../../environments/environment";
import {catchError, EMPTY, map, Observable} from "rxjs";
import {IVehicle} from "../../Models/vehicle";
import {MessageService} from "./message.service";

@Injectable({
  providedIn: 'root'
})
export class VehiclesService {

  private url: string = environment.baseUrl

  constructor(
    private http: HttpClient,
    private msgService: MessageService
  ) {
  }

  public getAllVehicles(): Observable<IVehicle[]> {
    return this.http.get(this.url + '/car/all').pipe(
      map(response => {
        return response as IVehicle[]
      }),catchError(err => this.errHandler(err))
    )
  }
  public getVehicleById(id: string | null): Observable<IVehicle[]>{
    return this.http.get(this.url + '/car/' + id).pipe(
      map(response => {
        return response as IVehicle[]
      }),catchError(err => this.errHandler(err))
    )
  }
  public deleteVehicle(id: number): Observable<unknown>{
    return this.http.delete(this.url + '/car/delete/' + id).pipe(
      catchError(err => this.errHandler(err))
    )
  }
  public addVehicle(vehicle: IVehicle): Observable<string>{
    return this.http.post(this.url + '/car/new', vehicle).pipe(
      map(response => {
        return response as string
      }),catchError(err => this.errHandler(err))
    )
  }
  public updateVehicle(id: number, vehicle: IVehicle){
     return this.http.put(this.url + '/car/update/' + id,vehicle).pipe(
       map(response => {
         return response
       }),catchError(err => this.errHandler(err))
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
